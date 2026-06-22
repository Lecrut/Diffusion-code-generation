VALIDATION_THRESHOLD = 0
INPUT_ERROR_MSG = "Input must be a non-negative integer"
TYPE_ERROR_MSG = "Input must be an integer"
ACCUMULATOR_INIT = 1
LOOP_START = 2

def compute_factorial(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(TYPE_ERROR_MSG)
    if n < VALIDATION_THRESHOLD:
        raise ValueError(INPUT_ERROR_MSG)
    result = ACCUMULATOR_INIT
    for multiplier in range(LOOP_START, n + 1):
        result *= multiplier
    return result

if __name__ == '__main__':
    test_inputs = [0, 1, 5, 10, 15]
    for num in test_inputs:
        print(compute_factorial(num))
    try:
        compute_factorial(-5)
    except ValueError as e:
        print(str(e))
    try:
        compute_factorial(3.14)
    except TypeError as e:
        print(str(e))