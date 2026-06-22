def check_integers(a, b, c):
    if a == 0:
        raise ValueError("First integer cannot be zero for divisibility check")
    pos_a = a > 0
    even_b = b % 2 == 0
    divisible_c_by_a = c % a == 0
    return (pos_a, even_b, divisible_c_by_a)
if __name__ == '__main__':
    result = check_integers(-3, 7, 15)
    print(result)