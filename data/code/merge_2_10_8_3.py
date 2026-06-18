import json
def get_sort_key(record):
    age = record.get('age', 0)
    status = record.get('status', '')
    if age >= 65 and 'senior' in status.lower():
        return (1, -age)
    elif age < 30:
        return (-age, -len(status))
    else:
        return (2, age)
def sort_users(users):
    sorted_users = sorted(users, key=get_sort_key)
    return sorted_users
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'age': 75, 'status': 'senior'},
        {'id': 102, 'age': 25, 'status': 'active'},
        {'id': 103, 'age': 45, 'status': 'retired'},
        {'id': 104, 'age': 80, 'status': 'senior_vip'},
    ]
    result = sort_users(sample_data)
    print(json.dumps(result))