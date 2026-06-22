def print_unique_elements(lst):
    seen = set()
    unique = [x for x in lst if not (x in seen or seen.add(x))]
    print(unique)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 6]
    print_unique_elements(sample_list)