def print_unique_elements(lst):
    unique_elements = set(lst)
    for element in unique_elements:
        print(element)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 6]
    print_unique_elements(sample_list)