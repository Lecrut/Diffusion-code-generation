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
    print("Original set of unique student names (stored in a set for uniqueness and fast membership testing):")
    print(student_names)
    print("\nTesting lookups:")
    search_term = "Alice"
    results = find_names(search_term)
    print(f"Names containing '{search_term}': {results}")
    search_term_2 = "Bob"
    results_2 = find_names(search_term_2)
    print(f"Names containing '{search_term_2}': {results_2}")
    search_term_3 = "X"
    results_3 = find_names(search_term_3)
    print(f"Names containing '{search_term_3}': {results_3}")