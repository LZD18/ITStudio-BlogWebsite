from django.db import models
from django.contrib.auth.models import User
import time
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

MEDIA_ADDR = "https://localhost:8000/images/"

sex = {
    "male": "男",
    "female": "女",
    "unknown": "保密"
}

class BlogUser(User, models.Model):
    nickname = models.CharField("昵称", max_length=50, default=f"OUCer_{int(time.time())}", unique=True)
    avatar   = ProcessedImageField(verbose_name="头像", upload_to='avatars/%Y/%m/%d', default='avatars/default.png', processors=[ResizeToFill(160, 160)])
    info     = models.TextField("简介", blank=True, null=True)
    birthday = models.DateField("生日", null=True, blank=True)
    reg_time = models.DateField("注册时间", auto_now_add=True, editable=False)
    sex      = models.CharField("性别", default="unknown", choices=sex, max_length=8)

    def get_avatar(self):
        return MEDIA_ADDR + str(self.avatar)