def find_print_index(target: str) -> int | None:
    print_list = ["apple", "banana", "cherry", "date"]
    for i, item in enumerate(print_list):
        if item == target:
            return i
    return None
if __name__ == '__main__':
    result = find_print_index("banana")
    print(f"Index of 'banana' is {result}")