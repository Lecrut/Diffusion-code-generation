def compare_numbers(first_integer, second_integer):
    return first_integer > second_integer

if __name__ == '__main__':
    number_one = 100
    number_two = 50
    is_number_one_larger = compare_numbers(number_one, number_two)
    print(is_number_one_larger)