def print_unique_elements(input_list):
    unique_elements = set(input_list)
    for item in unique_elements:
        print(item)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 6]
    print("Unique elements:")
    print_unique_elements(sample_list)