import time
student_names = {
    "Alice Smith",
    "Bob Johnson",
    "Charlie Brown",
    "Alice Smith",
    "Diana Prince",
    "Bob Johnson",
    "Eve Adams"
}
def find_names(target):
    found = []
    for name in student_names:
        if target in name:
            found.append(name)
    return found
if __name__ == '__main__':
    print(f"Original set of unique names stored: {student_names}")
    print("\nChecking for 'Alice Smith':")
    print("Existence check:", "Alice Smith" in student_names)
    print("\nChecking for 'Frank Miller':")
    print("Existence check:", "Frank Miller" in student_names)
    search_term = "Alice"
    print(f"\nSearching for names containing '{search_term}':")
    results = find_names(search_term)
    print(results)
    print("\nSet size after initialization:", len(student_names))