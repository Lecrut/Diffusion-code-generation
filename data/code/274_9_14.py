def print_unique_elements(lst):
    seen = set()
    unique = []
    for num in lst:
        if num not in seen:
            unique.append(num)
            seen.add(num)
    return unique

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3, 6]
    print(print_unique_elements(sample_list))