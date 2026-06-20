THRESHOLD = 10 ** 20

def multiply_large_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Both inputs must be integers')
    if abs(a * b) < THRESHOLD:
        return a * b
    result = 0
    for digit in str(b):
        if digit == '0':
            continue
        multiplier = int(digit)
        part = a * 10 ** len(str(multiplier))
        result += multiply_large_integers(part, multiplier)
    return result
if __name__ == '__main__':
    result = multiply_large_integers(12345678901234567890, 98765432109876543210)
    print(result)