def greater_of_two(a, b):

    def validate_inputs(x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError('Both inputs must be integers')
    validate_inputs(a, b)
    difference = a - b
    mask = difference >> 31 & 1
    return a - mask * difference
if __name__ == '__main__':
    num1 = 55
    num2 = 38
    result = greater_of_two(num1, num2)
    print(result)