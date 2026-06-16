def is_odd(n):
    return n & 1 != 0
if __name__ == '__main__':
    samples = [-5, -2, 0, 3, 7]
    for val in samples:
        print(f"{val} is odd: {is_odd(val)}")