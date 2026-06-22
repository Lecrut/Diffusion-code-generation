def print_integers(integer_list):
    if not all(isinstance(item, int) for item in integer_list):
        raise ValueError("All elements must be integers")
    for number in integer_list:
        print(number)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        print_integers(sample_values)
    except ValueError as e:
        print(e)