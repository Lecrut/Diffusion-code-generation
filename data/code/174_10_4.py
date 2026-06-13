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
        profile = user_profiles[name_to_find]
        print(f"Profile for {name_to_find}:")
        print(f"Age: {profile['age']}")
        print(f"City: {profile['city']}")
    else:
        print(f"{name_to_find} not found.")
    print("\n--- Iterating Through All Profiles ---")
    for name, data in user_profiles.items():
        print(f"Name: {name}, Age: {data['age']}, City: {data['city']}")
if __name__ == '__main__':
    main()