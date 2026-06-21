class UserIDMapper:
    def __init__(self):
        self.user_to_index = {}
        self.index_to_user = {}

    def add_user(self, user_id):
        if user_id not in self.user_to_index:
            index = len(self.user_to_index)
            self.user_to_index[user_id] = index
            self.index_to_user[index] = user_id

    def get_index(self, user_id):
        return self.user_to_index.get(user_id, -1)

    def get_user(self, index):
        return self.index_to_user.get(index, None)

if __name__ == '__main__':
    mapper = UserIDMapper()
    users = ["user1", "user2", "user3"]
    for user in users:
        mapper.add_user(user)
    
    print("User to Index Mapping:", mapper.user_to_index)
    print("Index to User Mapping:", mapper.index_to_user)
    print("Index of 'user2':", mapper.get_index("user2"))
    print("User at index 1:", mapper.get_user(1))