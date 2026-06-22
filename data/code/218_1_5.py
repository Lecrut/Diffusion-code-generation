def find_min_element(input_tuple):
    min_element = input_tuple[0]
    for element in input_tuple:
        if element < min_element:
            min_element = element
    return min_element

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 7)
    print(find_min_element(sample_tuple))