def reverse_elements(elements):
    reversed_elements = []
    for element in elements:
        reversed_elements.insert(0, element)
    return reversed_elements

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    reversed_values = reverse_elements(sample_values)
    print(reversed_values)