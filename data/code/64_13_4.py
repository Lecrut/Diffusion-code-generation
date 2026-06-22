def power_mod(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def large_power(base, exponent):
    return base ** exponent

if __name__ == '__main__':
    print(power_mod(2, 10, 1000))
    print(power_mod(3, 100, 7))
    print(power_mod(123456789, 987654321, 1000000007))
    print(large_power(2, 1000))
    print(large_power(10, 50))