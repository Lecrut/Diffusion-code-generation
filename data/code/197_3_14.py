class AuthorizationChecker:
    AUTHORIZED_MEMBERS = {'user1': True, 'user2': True, 'user3': True}

    @staticmethod
    def is_user_authorized(user_id):
        return user_id in AuthorizationChecker.AUTHORIZED_MEMBERS

if __name__ == '__main__':
    print(AuthorizationChecker.is_user_authorized('user2'))
    print(AuthorizationChecker.is_user_authorized('user4'))