def main():
    user_profiles = {
        "Alice": {"age": 30, "city": "New York"},
        "Bob": {"age": 25, "city": "Los Angeles"},
        "Charlie": {"age": 35, "city": "Chicago"}
    }
    print("--- Storing User Profiles ---")
    print(user_profiles)
    print("\n--- Retrieving Specific Information ---")
    name_to_find = "Bob"
    if name_to_find in user_profiles:
        bob_info = user_profiles[name_to_find]
        print(f"Profile for {name_to_find}:")
        print(f"Age: {bob_info['age']}")
        print(f"City: {bob_info['city']}")
    else:
        print(f"{name_to_find} not found.")
    print("\n--- Iterating Through All Profiles ---")
    for name, details in user_profiles.items():
        print(f"Name: {name}, Age: {details['age']}, City: {details['city']}")
if __name__ == '__main__':
    main()