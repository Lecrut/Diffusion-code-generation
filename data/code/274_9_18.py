def print_unique_elements(lst):
    unique_set = set(lst)
    for item in unique_set:
        print(item)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3]
    print_unique_elements(sample_list)