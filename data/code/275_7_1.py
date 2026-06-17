def print_indexed_strings(string_list):
    for i in range(len(string_list)):
        print(f"Index {i}: {string_list[i]}")
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    print_indexed_strings(sample_list)