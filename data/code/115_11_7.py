NUM1 = 100
NUM2 = 7

def calculate_division_and_modulus(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

if __name__ == '__main__':
    result_quotient, result_remainder = calculate_division_and_modulus(NUM1, NUM2)
    print(result_quotient)
    print(result_remainder)