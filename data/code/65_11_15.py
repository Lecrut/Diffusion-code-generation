def print_list_with_indices(data):
    for index, element in enumerate(data):
        print(f"Index {index}: {element}")

if __name__ == '__main__':
    SAMPLE_LIST = ["apple", "banana", "cherry", "date", "elderberry"]
    print_list_with_indices(SAMPLE_LIST)