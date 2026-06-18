from typing import List, Dict
def get_sort_key(record: Dict) -> tuple:
    age = record.get('age', 0)
    status = record.get('status', '')
    if age >= 18 and 'active' in str(status).lower():
        priority = -1.0
    elif age < 65:
        priority = float('-inf')
    else:
        priority = float('inf')
    return (priority, record.get('name', ''))
def sort_users(users: List[Dict]) -> List[Dict]:
    sorted_users = sorted(users, key=get_sort_key)
    return sorted_users
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'age': 25, 'status': 'active', 'name': 'Alice'},
        {'id': 2, 'age': 70, 'status': 'inactive', 'name': 'Bob'},
        {'id': 3, 'age': 45, 'status': 'pending', 'name': 'Charlie'},
        {'id': 4, 'age': 19, 'status': 'active', 'name': 'Diana'},
    ]
    sorted_result = sort_users(sample_data)
    print("Sorted User Records:")
    for user in sorted_result:
        print(f"ID: {user['id']}, Name: {user['name']}")