def validate_inputs(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("All inputs must be integers")
    return True

def check_positivity(value):
    return value > 0

def check_evenness(value):
    return value % 2 == 0

def check_divisibility(dividend, divisor):
    if divisor == 0:
        return False
    return dividend % divisor == 0

def analyze_integers(a, b, c):
    validate_inputs(a, b, c)
    pos_result = check_positivity(a)
    even_result = check_evenness(b)
    div_result = check_divisibility(c, a)
    return (pos_result, even_result, div_result)

if __name__ == '__main__':
    sample_a = 5
    sample_b = 10
    sample_c = 20
    result = analyze_integers(sample_a, sample_b, sample_c)
    print(result)