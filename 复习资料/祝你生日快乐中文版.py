
age=int(input('嘿，你今年多大了='))
first_name=str(input('啊哈，那你姓啥呀='))
last_name=str(input('嗯嗯，知道了，那你的名呢？='))
first_name=first_name.strip()
last_name=last_name.strip()
full_name=first_name+" "+last_name
full_name=full_name.title()
full_name=str(full_name)
message="祝你" + str(age) + "'岁生日快乐!"
print(message+full_name)
