def main():
    user_profiles = {
        "alice": {"name": "Alice", "age": 30, "city": "New York"},
        "bob": {"name": "Bob", "age": 25, "city": "Los Angeles"},
        "charlie": {"name": "Charlie", "age": 35, "city": "Chicago"}
    }
    print("--- Storing User Profiles ---")
    print(user_profiles)
    print("\n--- Retrieving Specific Information ---")
    user_id = "bob"
    if user_id in user_profiles:
        profile = user_profiles[user_id]
        print(f"Profile for {user_id}:")
        print(f"Name: {profile['name']}")
        print(f"Age: {profile['age']}")
        print(f"City: {profile['city']}")
    else:
        print(f"User {user_id} not found.")
    print("\n--- Iterating Through All Profiles ---")
    for user_id, profile in user_profiles.items():
        print(f"User ID: {user_id}, Name: {profile['name']}, Age: {profile['age']}, City: {profile['city']}")
if __name__ == '__main__':
    main()