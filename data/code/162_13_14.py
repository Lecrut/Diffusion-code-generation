class UserIDMapper:

    def __init__(self):
        self.user_to_index = {}

    def add_user(self, user_id):
        if user_id not in self.user_to_index:
            index = len(self.user_to_index)
            self.user_to_index[user_id] = index

    def get_index(self, user_id):
        return self.user_to_index.get(user_id, None)
if __name__ == '__main__':
    mapper = UserIDMapper()
    users = ['user1', 'user2', 'user3']
    for user in users:
        mapper.add_user(user)
    print(mapper.get_index('user1'))
    print(mapper.get_index('user2'))
    print(mapper.get_index('user3'))
    print(mapper.get_index('user4'))