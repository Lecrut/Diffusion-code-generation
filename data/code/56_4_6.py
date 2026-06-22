import itertools
import operator

def print_multiplication_table(n, limit=10):
    return '\n'.join([f'{n} x {i} = {n * i}' for i in range(1, limit + 1)])

if __name__ == '__main__':
    print(print_multiplication_table(5))