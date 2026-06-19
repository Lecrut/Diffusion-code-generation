def print_elements_with_index(elements):
    for index, element in enumerate(elements):
        print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    mixed_data = [42, "hello", 3.14, True, None, {'key': 'value'}, [1, 2, 3]]
    print_elements_with_index(mixed_data)