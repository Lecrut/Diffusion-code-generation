def validate_input(data):
    if not all(isinstance(item, int) for item in data):
        raise ValueError("All elements must be integers")

def print_integers(integer_list):
    validate_input(integer_list)
    for number in integer_list:
        print(number)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print_integers(sample_values)