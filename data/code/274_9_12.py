def print_unique_elements(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            print(item)
            seen.add(item)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 6]
    print_unique_elements(sample_list)