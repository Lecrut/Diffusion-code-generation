def print_multiplication_table(n=5, start=1, end=10):
    return [f"{n} x {i} = {n * i}" for i in range(start, end + 1)]

if __name__ == '__main__':
    print('\n'.join(print_multiplication_table()))