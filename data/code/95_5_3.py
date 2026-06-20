def check_integers(a, b, c):
    if not all(isinstance(x, int) for x in [a, b, c]):
        raise ValueError("All inputs must be integers")
    pos_a = a > 0
    even_b = b % 2 == 0
    divisible_c_by_a = c % a == 0
    return (pos_a, even_b, divisible_c_by_a)

if __name__ == '__main__':
    result = check_integers(15, 22, 60)
    print(result)