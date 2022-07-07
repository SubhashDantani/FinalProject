# Generated by Django 3.1.8 on 2022-07-06 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(default='', max_length=200)),
                ('c_email', models.EmailField(default='', max_length=200)),
                ('c_cno', models.CharField(default='', max_length=50)),
                ('c_add', models.TextField(default='')),
                ('join_date', models.DateField(auto_now=True, null=True)),
                ('profile', models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='Com_Prof/')),
                ('c_pass', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Company_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_nm', models.CharField(default='', max_length=200)),
                ('prod_price', models.PositiveIntegerField(default=0)),
                ('prod_qty', models.PositiveIntegerField(default=0)),
                ('prod_img', models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='ProductPic/')),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_details')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_nm', models.CharField(default='', max_length=200)),
                ('cust_em', models.EmailField(default='', max_length=200)),
                ('cust_con', models.CharField(default='', max_length=50)),
                ('cust_add1', models.TextField(default='')),
                ('cust_add2', models.TextField(default='')),
                ('cust_pass', models.CharField(default='', max_length=200)),
                ('cust_regi_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cust_profile', models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='Cust_Pic/')),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_details')),
            ],
        ),
    ]
