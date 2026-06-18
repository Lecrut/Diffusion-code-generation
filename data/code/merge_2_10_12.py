from dataclasses import dataclass
@dataclass(order=True)
class User:
    name: str = ""
    age: int = 0
def sort_users(users: list[User], criteria: dict[str, bool]) -> list[User]:
    return sorted(users, key=lambda u: tuple(getattr(u, k) if not v else -getattr(u, k) for k, v in criteria.items()))
if __name__ == '__main__':
    users = [
        User(name="Alice", age=30),
        User(name="Bob", age=25),
        User(name="Charlie", age=35),
        User(name="David", age=28),
    ]
    sorted_users = sort_users(users, {"age": True, "name": False})
    for user in sorted_users:
        print(f"{user.name}: {user.age}")