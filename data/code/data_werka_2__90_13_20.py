def check_either_above_threshold(value_a, value_b, threshold=10):
    if not isinstance(value_a, int) or not isinstance(value_b, int):
        raise ValueError("Inputs must be integers")
    return value_a > threshold or value_b > threshold

if __name__ == '__main__':
    num_one = 15
    num_two = 4
    result = check_either_above_threshold(num_one, num_two)
    print(result)