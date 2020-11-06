from django.db import models

# Create your models here.
from django.db import models

#1.类名的首字母必须大写
#2.类必须继承models.Model
#3.models类定义的字段类型

class Example(models.Model):    #类名就是数据库名，继承models的方法
    name = models.CharField(max_length=32, verbose_name='案例的名称') #变量名对应字段名
    type = models.CharField(max_length=32, verbose_name='案例类型')

    def __str__(self):
        return "%s:%s" % (self.name,self.type)