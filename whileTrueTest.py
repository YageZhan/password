#===================================================
# 密码重试程式
#password是a123456
#让使用者重复输入密码
#最多输入3次
#如果正确 就引出“登陆成功”
#如果不正确 就引出“密码错误！还有____次机会！


password = 'a123456' #数字的东西通常存一次就好
i = 3 #回圈次数
while True:  #或写成 while i > 0:
	pwd = input('请输入密码： ')
	if pwd == password:
		print('登录成功！')
		break
	else:
		i = i - 1 #最多输入3次
		print('密码错误！还有', i, '次机会！') #注意看，很讲究，内容用逗号隔开
		if i == 0: #剩余机会是0的时候break
			break

# =================或者写成================================
password = 'a123456' #数字的东西通常存一次就好
i = 3 #回圈次数
while i > 0:
	i = i - 1 #最多输入3次，减少剩余次数；每问一次密码就减少一次机会
	pwd = input('请输入密码： ')
	if pwd == password:
		print('登录成功！')
		break
	else:
		print('密码错误!')
		if i > 0:
			print('还有', i, '次机会！')
		else:
			print('没有机会了，要锁帐号了！')
		