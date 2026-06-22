SAMPLE_VALUE = 10
MULTIPLIER = 2

def compute_exponent(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def get_square(side_length):
    return compute_exponent(side_length, MULTIPLIER)

if __name__ == '__main__':
    val = SAMPLE_VALUE
    output = get_square(val)
    print(output)