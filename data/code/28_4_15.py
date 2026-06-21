def validate_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    return [a, b]

def sort_values_in_descending_order(first_val, second_val):
    raw_list = validate_integers(first_val, second_val)
    return sorted(raw_list, reverse=True)

if __name__ == '__main__':
    num_a = 99
    num_b = 45
    output = sort_values_in_descending_order(num_a, num_b)
    print(output)