def check_integers(a, b, c):
    pos_a = a > 0
    even_b = b % 2 == 0
    divisible_c_by_a = c % a == 0
    return (pos_a, even_b, divisible_c_by_a)
if __name__ == '__main__':
    result = check_integers(10, 12, 30)
    print(result)