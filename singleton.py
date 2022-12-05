def singleton(cls):

    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return wrap

@singleton
class User(object):
    def __init__(self,username):
        self.username = username

if __name__ == '__main__':
    user1 = User('omar')
    user2 = User('OMAR')
    
    print(user1 is user2)
    print(user1)