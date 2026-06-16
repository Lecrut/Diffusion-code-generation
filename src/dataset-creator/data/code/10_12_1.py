from typing import List, Any
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
def sort_users(users: List[User], criteria: List[tuple]) -> List[User]:
    for field, direction in reversed(criteria):
        users.sort(key=lambda u: getattr(u, field), reverse=(direction == 'desc'))
    return users
if __name__ == '__main__':
    sample_users = [
        User("Alice", 30),
        User("Bob", 25),
        User("Charlie", 35),
        User("Diana", 28)
    ]
    sort_order = [("age", "desc"), ("name", "asc")]
    sorted_users = sort_users(sample_users, sort_order)
    for user in sorted_users:
        print(f"{user.name}: {user.age}")