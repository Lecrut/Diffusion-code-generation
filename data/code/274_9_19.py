def print_unique_elements(lst):
    seen = set()
    for num in lst:
        if num not in seen:
            print(num)
            seen.add(num)

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print_unique_elements(sample_list)