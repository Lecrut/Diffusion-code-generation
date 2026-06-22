REQUIRED_THRESHOLD = 3
EVEN_DIVISOR = 2
POSITIVE_BOUNDARY = 0

def has_minimum_positive_even_divisible(items):
    qualifying_count = 0
    for value in items:
        is_positive = value > POSITIVE_BOUNDARY
        is_even = value % EVEN_DIVISOR == 0
        if is_positive and is_even:
            qualifying_count += 1
    return qualifying_count >= REQUIRED_THRESHOLD

if __name__ == '__main__':
    data_set_one = [2, 4, 6, 1, 3, 5]
    data_set_two = [1, 3, 5, 7, 9]
    data_set_three = [2, 4, 6, 8, 10]
    data_set_four = [-2, -4, -6, 8, 10]
    
    result_one = has_minimum_positive_even_divisible(data_set_one)
    result_two = has_minimum_positive_even_divisible(data_set_two)
    result_three = has_minimum_positive_even_divisible(data_set_three)
    result_four = has_minimum_positive_even_divisible(data_set_four)
    
    print(result_one)
    print(result_two)
    print(result_three)
    print(result_four)