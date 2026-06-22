def print_list_with_index(lst):
    for i, item in enumerate(lst, start=1):
        print(f"{i}: {item}")

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    print_list_with_index(sample_values)