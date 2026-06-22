def print_unique_elements(lst):
    seen = set()
    unique = [x for x in lst if not (x in seen or seen.add(x))]
    for item in unique:
        print(item)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
    print_unique_elements(sample_list)