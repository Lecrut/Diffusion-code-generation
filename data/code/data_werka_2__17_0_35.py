EVEN_MODULO = 2

def is_even(n):
    return n % EVEN_MODULO == 0

if __name__ == '__main__':
    sample_values = [10, -3, 8, 7, 0, -5]
    for value in sample_values:
        print(is_even(value))