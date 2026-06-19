def print_elements_with_index(elements):
    for index in range(len(elements)):
        element = elements[index]
        print(f"Index: {index}, Element: {element}")

if __name__ == '__main__':
    mixed_data = [100, "text", 1.618, False, None, {'z': 'w'}, (1, 2)]
    print_elements_with_index(mixed_data)