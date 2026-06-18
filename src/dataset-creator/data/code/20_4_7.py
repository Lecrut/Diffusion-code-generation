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
    print("Original set of unique student names stored:")
    print(student_names)
    print("\nSearching for names containing 'Alice':")
    results_alice = find_names("Alice")
    print(results_alice)
    print("\nSearching for names containing 'Bob':")
    results_bob = find_names("Bob")
    print(results_bob)
    print("\nSearching for names containing 'Charlie':")
    results_charlie = find_names("Charlie")
    print(results_charlie)