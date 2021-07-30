###Short URL Generator###
data_storage={}
new_id=2020
while 1:
    print("Enter the selection:\n 1.Generate URL \n 2.Get the URL")
    S=input("choice:")
    if(S=="1"):
        u=input("Enter the URL:")
        new_id+=1#incremented by one for every selection
        data_storage[new_id]=u
        print("Your short URL :",new_id)#short url
    else:
        u=int(input("Enter the ID:"))#enter the url id you will get the exact original URL
        print("URL:",data_storage[u])#original url
    
