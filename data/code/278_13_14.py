def validate_input(input_list):
    if not all(isinstance(item, int) for item in input_list):
        raise ValueError("All items in the list must be integers")

def print_integers(integer_list):
    validate_input(integer_list)
    for number in integer_list:
        print(number)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print_integers(sample_values)