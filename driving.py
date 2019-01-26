contry = input('請問你是哪國人: ')
age = input('請輸入你的年齡: ')
age = int(age)
if contry == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif contry == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('不在此次調查之內')
