import hashlib, threading, sys

HASH = '31143FA833B08E456C6A3EDCAF88B74EC08B28C4DDC867CBF5AF2B795DC2C9DA' #24338755
password_found = False

def sha256(password=''):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password.upper()

def bruteforce(begin, end):
    global password_found
    if password_found == False:
        for i in range(begin,end):
            num = str(i)
            hashed_num = sha256(num)
            #print('Cechking for password: ' + num + ' ----> ' + hashed_num)
            if hashed_num == HASH:
                print('Password found: ' + num)
                password_found = True
            if password_found:
                break
                sys.exit(0)
    else: 
        print("\n The password was found")


begin = 10000000
end = 11153846
threads = []
for i in range(78):
    t = threading.Thread(target=bruteforce, args=(begin, end))
    threads.append(t)
    t.start()
    begin = end
    end = end + 1153846

