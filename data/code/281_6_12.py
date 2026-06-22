def sum_n_integers(n):
    if not isinstance(n, int) or n != 9:
        raise ValueError("Input must be exactly 9")
    return sum(range(1, 10))

if __name__ == '__main__':
    result = sum_n_integers(9)
    print(result)