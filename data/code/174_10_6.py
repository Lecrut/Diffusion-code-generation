def main():
    user_profiles = {
        "alice": {"name": "Alice", "age": 30, "city": "New York"},
        "bob": {"name": "Bob", "age": 25, "city": "Los Angeles"},
        "charlie": {"name": "Charlie", "age": 35, "city": "Chicago"}
    }
    print("--- Storing User Profiles ---")
    print(user_profiles)
    print("\n--- Retrieving Information for Alice ---")
    alice_info = user_profiles.get("alice")
    if alice_info:
        print(f"Name: {alice_info['name']}")
        print(f"Age: {alice_info['age']}")
        print(f"City: {alice_info['city']}")
    else:
        print("Alice not found.")
    print("\n--- Retrieving Information for Bob ---")
    bob_info = user_profiles.get("bob")
    if bob_info:
        print(f"Name: {bob_info['name']}")
        print(f"Age: {bob_info['age']}")
        print(f"City: {bob_info['city']}")
    else:
        print("Bob not found.")
    print("\n--- Attempting to retrieve non-existent user ---")
    dave_info = user_profiles.get("dave")
    if dave_info:
        print(f"Name: {dave_info['name']}")
    else:
        print("Dave not found.")
if __name__ == '__main__':
    main()