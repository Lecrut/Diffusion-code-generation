EVEN_MODULO = 2

def check_even(n):
    return n % EVEN_MODULO == 0

if __name__ == '__main__':
    sample_values = [10, 15, 22]
    for value in sample_values:
        print(check_even(value))