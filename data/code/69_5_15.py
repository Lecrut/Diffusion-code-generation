def print_elements_with_index(elements):
    for index in range(len(elements)):
        print(f"Index {index}: {elements[index]}")

if __name__ == '__main__':
    mixed_data = [42, "hello", 3.14, True, None]
    print_elements_with_index(mixed_data)