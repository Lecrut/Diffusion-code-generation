class UserAuthorization:
    def __init__(self):
        self.authorized_members = {'user1': True, 'user2': True, 'user3': True}

    def is_user_authorized(self, user_id):
        return self.authorized_members.get(user_id, False)

if __name__ == '__main__':
    auth_checker = UserAuthorization()
    print(auth_checker.is_user_authorized('user2'))
    print(auth_checker.is_user_authorized('user4'))