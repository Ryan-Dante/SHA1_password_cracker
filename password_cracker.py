import hashlib

def crack_sha1_hash(hash, use_salts=False):
    with open('top-10000-passwords.txt', 'rb') as file:
        arr = []
        for password in file:
            password = password.strip()
            if hashlib.sha1(password).hexdigest() == hash:
                return password.decode('utf-8')
            
            if use_salts:
                with open('known-salts.txt', 'rb') as salts:
                    for salt in salts:
                        salt = salt.strip()
                        if hashlib.sha1(salt + password).hexdigest() == hash:
                            return password.decode('utf-8')
                        if hashlib.sha1(password + salt).hexdigest() == hash:
                            return password.decode('utf-8')
                        if hashlib.sha1(salt + password + salt).hexdigest() == hash:
                            return password.decode('utf-8')
            arr.append(password)

    return "PASSWORD NOT IN DATABASE"


  