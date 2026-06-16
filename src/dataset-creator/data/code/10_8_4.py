from typing import List, Dict
def get_sort_key(record: Dict) -> tuple:
    if record['status'] == 'active':
        return (0, -record['age'])                                         
    else:
        return (1, record['age'])                                          
def sort_users(users: List[Dict]) -> List[Dict]:
    return sorted(users, key=get_sort_key)
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25, 'status': 'active'},
        {'id': 2, 'name': 'Bob', 'age': 30, 'status': 'inactive'},
        {'id': 3, 'name': 'Charlie', 'age': 20, 'status': 'active'},
        {'id': 4, 'name': 'Diana', 'age': 35, 'status': 'inactive'},
    ]
    sorted_users = sort_users(sample_data)
    for user in sorted_users:
        print(f"{user['name']} ({user['age']}) - {user['status']}")