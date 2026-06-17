def print_with_index(string_list):
    for i in range(len(string_list)):
        print(f"Index {i}: {string_list[i]}")
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    print_with_index(sample_list)