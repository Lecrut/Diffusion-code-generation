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
    print("Original set of unique student names (stored as a set for uniqueness):")
    print(student_names)
    print("-" * 30)
    target1 = "Alice"
    start_time = time.time()
    results1 = find_names(target1)
    end_time = time.time()
    print(f"Searching for names containing '{target1}': {results1}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("-" * 30)
    target2 = "Bob"
    start_time = time.time()
    results2 = find_names(target2)
    end_time = time.time()
    print(f"Searching for names containing '{target2}': {results2}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("-" * 30)
    target3 = "X"
    start_time = time.time()
    results3 = find_names(target3)
    end_time = time.time()
    print(f"Searching for names containing '{target3}': {results3}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")