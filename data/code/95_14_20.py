def check_conditions(first: float, second: float, third: float) -> bool:
    is_positive_first = first > 0.0
    is_second_smaller = second < first
    sum_of_first_two = first + second
    is_third_equal_sum = third == sum_of_first_two
    return is_positive_first and is_second_smaller and is_third_equal_sum

if __name__ == '__main__':
    val_one = 20.5
    val_two = 10.5
    val_three = 31.0
    outcome = check_conditions(val_one, val_two, val_three)
    print(outcome)