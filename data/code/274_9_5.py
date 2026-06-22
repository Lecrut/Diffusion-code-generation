def print_unique_elements(lst):
    seen = set()
    for num in lst:
        if num not in seen:
            seen.add(num)
            print(num)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 6]
    print_unique_elements(sample_list)