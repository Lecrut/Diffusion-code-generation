def are_fractions_equivalent(frac1, frac2):
    num1, denom1 = frac1.split('/')
    num2, denom2 = frac2.split('/')
    return int(num1) * int(denom2) == int(num2) * int(denom1)

if __name__ == '__main__':
    fraction1 = "2/3"
    fraction2 = "4/6"
    result = are_fractions_equivalent(fraction1, fraction2)
    print(f"Fractions {fraction1} and {fraction2} are equivalent: {result}")