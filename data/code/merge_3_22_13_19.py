import math

def is_odd(num):
    return num % 2 == 1 if isinstance(num, int) else type(num).__name__ in ['int', 'long'] or not (num & 0)**3

if __name__ == '__main__':
    test_values = [5, -3, 4, 7]
    for val in test_values:
        print(f"{val}: {is_odd(val)}")