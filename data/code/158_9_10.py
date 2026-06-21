odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15}

def validate_odd_set(odd_set):
    if not isinstance(odd_set, set):
        raise ValueError("Input must be a set.")
    if any(x % 2 == 0 for x in odd_set):
        raise ValueError("Set contains even numbers.")

def find_even_numbers(odd_set):
    validate_odd_set(odd_set)
    all_numbers = set(range(1, 16))
    return all_numbers - odd_set

if __name__ == '__main__':
    even_numbers = find_even_numbers(odd_numbers)
    print(even_numbers)