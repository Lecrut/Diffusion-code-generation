users = [
    {"id": 1, "age": 25, "status": "active"},
    {"id": 2, "age": 30, "status": "inactive"},
    {"id": 3, "age": 45, "status": "active"},
    {"id": 4, "age": 18, "status": "pending"},
]
def get_sort_key(user):
    if user["age"] >= 20 and user["status"] == "active":
        return (0, -user["age"])
    elif user["age"] < 20:
        return (1, -user["id"])
    else:
        return (2, user["id"])
sorted_users = sorted(users, key=get_sort_key)
if __name__ == '__main__':
    for user in sorted_users:
        print(f"ID: {user['id']}, Age: {user['age']}, Status: {user['status']}")