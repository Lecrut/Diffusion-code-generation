import json
def get_sort_key(record):
    age = record.get('age', 0)
    status = record.get('status', '')
    if status == 'active':
        return (1, -age)
    elif status == 'inactive':
        return (2, age)
    else:
        return (3, 0)
def sort_users(users):
    sorted_users = sorted(users, key=get_sort_key)
    return sorted_users
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25, 'status': 'active'},
        {'id': 2, 'name': 'Bob', 'age': 30, 'status': 'inactive'},
        {'id': 3, 'name': 'Charlie', 'age': 18, 'status': 'active'},
        {'id': 4, 'name': 'Diana', 'age': 25, 'status': 'unknown'},
    ]
    sorted_result = sort_users(sample_data)
    print(json.dumps(sorted_result))