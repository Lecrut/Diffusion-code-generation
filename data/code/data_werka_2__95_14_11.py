THINKING_COMPLETED
def check_conditions(first: float, second: float, third: float) -> bool:
    is_first_positive: bool = first > 0.0
    is_second_smaller: bool = second < first
    is_sum_equal: bool = third == first + second
    return is_first_positive and is_second_smaller and is_sum_equal
if __name__ == '__main__':
    result: bool = check_conditions(1.5, 0.5, 2.0)
    print(result)