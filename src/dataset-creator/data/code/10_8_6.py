from typing import List, Tuple
def get_sort_key(record: dict) -> int:
    if record['status'] == 'active':
        return -record['age']                                     
    else:
        return record['age']                                       
def sort_users(users: List[dict]) -> List[dict]:
    return sorted(users, key=get_sort_key)
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'age': 25, 'status': 'active'},
        {'id': 2, 'age': 30, 'status': 'inactive'},
        {'id': 3, 'age': 20, 'status': 'active'},
        {'id': 4, 'age': 35, 'status': 'inactive'},
    ]
    sorted_data = sort_users(sample_data)
    for user in sorted_data:
        print(f"ID: {user['id']}, Age: {user['age']}, Status: {user['status']}")