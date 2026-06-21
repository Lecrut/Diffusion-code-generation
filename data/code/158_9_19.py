odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15}

def compute_even_numbers(odd_set):
    all_numbers = set(range(1, 16))
    even_numbers = all_numbers - odd_set
    return even_numbers

if __name__ == '__main__':
    sample_odd_set = {2, 4, 6, 8, 10}
    even_numbers = compute_even_numbers(sample_odd_set)
    print(even_numbers)