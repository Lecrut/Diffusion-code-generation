def print_elements_with_index(elements):
    for index in range(len(elements)):
        element = elements[index]
        print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    mixed_data = [10, "world", 2.718, False, None, {'a': 'b'}, (4, 5, 6)]
    print_elements_with_index(mixed_data)