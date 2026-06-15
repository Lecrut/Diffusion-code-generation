def main():
    user_profiles = {
        "alice": {"name": "Alice", "age": 30, "city": "New York"},
        "bob": {"name": "Bob", "age": 25, "city": "Los Angeles"},
        "charlie": {"name": "Charlie", "age": 35, "city": "Chicago"}
    }
    print("--- Storing User Profiles ---")
    print(user_profiles)
    print("\n--- Retrieving Information for Alice ---")
    alice_data = user_profiles.get("alice")
    if alice_data:
        print(f"Name: {alice_data['name']}")
        print(f"Age: {alice_data['age']}")
        print(f"City: {alice_data['city']}")
    else:
        print("Alice not found.")
    print("\n--- Retrieving Information for Bob ---")
    bob_data = user_profiles.get("bob")
    if bob_data:
        print(f"Name: {bob_data['name']}")
        print(f"Age: {bob_data['age']}")
        print(f"City: {bob_data['city']}")
    else:
        print("Bob not found.")
    print("\n--- Attempting to retrieve non-existent user ---")
    dave_data = user_profiles.get("dave")
    if dave_data:
        print(f"Name: {dave_data['name']}")
    else:
        print("Dave not found.")
if __name__ == '__main__':
    main()