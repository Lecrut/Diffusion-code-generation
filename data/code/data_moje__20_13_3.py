def is_even_by_lookup(n, even_list):
    return n in even_list

if __name__ == '__main__':
    sample_values = [2, 4, 6, 8, 10]
    test_numbers = [0, 1, 2, 3, 4, 5, 10, 11, 100, 101]
    for number in test_numbers:
        result = is_even_by_lookup(number, sample_values)
        print(f"{number}: {result}")