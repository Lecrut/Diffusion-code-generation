def print_elements_with_index(elements):
    for index in range(len(elements)):
        element = elements[index]
        print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    mixed_data = [100, "test", 3.14159, True, None, {'key': 'value'}, (1, 2, 3)]
    print_elements_with_index(mixed_data)