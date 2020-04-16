import os

try:
    with open("all_link_post.txt", 'r') as file:
        links = file.readlines()
        for link in links:
            link = link.replace('\n', '')
            print('cmd /c "instatouch comments {} --count 2000"'.format(link))
            os.system('cmd /c "instatouch comments {} --count 2000"'.format(link))
            print("SUCEED")
    pass
except Exception as e:
    print("error : ",e)
    raise
