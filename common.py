def find_common_characters(msg1,msg2):
    user_string1=set(msg1)
    user_string2=set(msg2)
    list=set(user_string1) & set(user_string2)
    print ('common_characters are:{}'.format(list))
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
find_common_characters(msg1,msg2)