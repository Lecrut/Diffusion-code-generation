def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(num1, num2):
    divisor = gcd(num1, num2)
    return num1 // divisor, num2 // divisor

if __name__ == '__main__':
    numerator_a = 8
    denominator_b = 12
    simplified_numerator, simplified_denominator = simplify_ratio(numerator_a, denominator_b)
    print(f"Original Ratio: {numerator_a}:{denominator_b}")
    print(f"Simplified Ratio: {simplified_numerator}:{simplified_denominator}")