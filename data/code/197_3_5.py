class AuthorizationChecker:
    def __init__(self):
        self.authorized_members = ['user1', 'user2', 'user3']

    def is_user_authorized(self, user_id):
        return user_id in self.authorized_members

if __name__ == '__main__':
    checker = AuthorizationChecker()
    print(checker.is_user_authorized('user2'))
    print(checker.is_user_authorized('user4'))