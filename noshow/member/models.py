from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=20)
    dob = models.DateField(
        '생년월일',
        max_length=8,
    )
    cp = models.IntegerField(
        '휴대전화',
        max_length=11,
    )
