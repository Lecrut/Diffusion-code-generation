def sum_five_integers(a, b, c, d, e):
    if not all(isinstance(x, int) and -100 <= x <= 100 for x in [a, b, c, d, e]):
        raise ValueError("All inputs must be integers between -100 and 100")
    return a + b + c + d + e

if __name__ == '__main__':
    result = sum_five_integers(10, 25, 30, 5, 2)
    print(result)