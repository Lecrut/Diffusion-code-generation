def create_name_set(names):
    return set(name.lower().strip() for name in names)
if __name__ == '__main__':
    known_names = ["Alice", "Bob", "Charlie"]
    target_names = ["alice", "bob smith", "David", "Eve"]
    valid_count = 0
    invalid_count = 0
    for candidate in target_names:
        if candidate.lower().strip() in create_name_set(known_names):
            print(f"{candidate} is a known name.")
            valid_count += 1
        else:
            print(f"{candidate} is not found.")
            invalid_count += 1
    print(f"Total checked: {valid_count + invalid_count}")