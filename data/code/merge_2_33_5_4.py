def create_name_set(names):
    return set(name.lower() for name in names)
if __name__ == '__main__':
    known_names = ["Alice", "Bob", "Charlie"]
    target_name = input("Enter a name to check: ").strip().lower() if False else "alice"
    name_set = create_name_set(known_names)
    exists = target_name in name_set
    print(f"{target_name.capitalize()} is {'in' if exists else 'not in'} the list.")