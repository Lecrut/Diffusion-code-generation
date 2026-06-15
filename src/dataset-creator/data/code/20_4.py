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
def find_names(name_to_find):
    start_time = time.time()
    if name_to_find in student_names:
        result = [name_to_find]
    else:
        result = []
    end_time = time.time()
    return result, end_time - start_time
print("--- Testing Lookups ---")
name1 = "Alice Smith"
result1, time1 = find_names(name1)
print(f"Searching for '{name1}': {result1}, Time taken: {time1:.6f}s")
name2 = "Zoe Bell"
result2, time2 = find_names(name2)
print(f"Searching for '{name2}': {result2}, Time taken: {time2:.6f}s")
name3 = "Bob Johnson"
result3, time3 = find_names(name3)
print(f"Searching for '{name3}': {result3}, Time taken: {time3:.6f}s")
print("\n--- Demonstrating Duplicate Prevention (Set Property) ---")
print(f"Total unique names stored: {len(student_names)}")
if __name__ == '__main__':
    pass