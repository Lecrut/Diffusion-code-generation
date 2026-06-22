def print_unique_elements(lst):
    seen = set()
    unique = [x for x in lst if not (x in seen or seen.add(x))]
    for element in unique:
        print(element)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print_unique_elements(sample_list)