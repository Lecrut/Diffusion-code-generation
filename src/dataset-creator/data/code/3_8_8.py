def is_even(n):
    return (n & 1) == 0
if __name__ == '__main__':
    samples = [42, -5, 0, 7]
    for val in samples:
        print(f"{val} is even: {is_even(val)}")