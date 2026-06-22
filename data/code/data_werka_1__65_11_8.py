def iterate_and_print_with_index(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    for index, element in enumerate(data):
        print(f"Index {index}: {element}")

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    try:
        iterate_and_print_with_index(sample_list)
    except TypeError as e:
        print(e)