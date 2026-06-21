authorized_members = ['admin', 'moderator', 'editor']

def is_user_authorized(user_id):
    return user_id in authorized_members

if __name__ == '__main__':
    sample_users = ['admin', 'viewer', 'moderator']
    results = {user: is_user_authorized(user) for user in sample_users}
    print(results)