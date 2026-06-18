import random
def get_sort_key(record):
    age = record['age']
    status = record['status']
    if status == 'active':
        return (0, -age)
    elif status == 'inactive':
        return (1, 0)
    else:
        return (2, 0)
def sort_users(users):
    sorted_users = sorted(users, key=get_sort_key)
    return sorted_users
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'age': 30, 'status': 'active'},
        {'id': 2, 'age': 45, 'status': 'inactive'},
        {'id': 3, 'age': 25, 'status': 'active'},
        {'id': 4, 'age': 60, 'status': 'pending'},
        {'id': 5, 'age': 35, 'status': 'active'}
    ]
    sorted_result = sort_users(sample_data)
    for user in sorted_result:
        print(f"ID: {user['id']}, Age: {user['age']}, Status: {user['status']}")