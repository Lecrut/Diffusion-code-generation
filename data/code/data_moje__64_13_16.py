import math

def power_mod(base, exponent, modulus):
    if modulus == 1:
        return 0
    if exponent == 0:
        return 1
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def calculate_fermat_number_digit_sum(fermat_index):
    n = 1 << (fermat_index + 1)
    f_k = n - 1
    return f_k

if __name__ == '__main__':
    p_result = power_mod(2, 1000000007, 10 ** 9 + 7)
    print(p_result)
    f_digit_sum = calculate_fermat_number_digit_sum(4)
    print(f_digit_sum)