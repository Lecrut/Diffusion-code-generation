EVEN_CHECK_THRESHOLD = 2

def is_even(n):
    return n % EVEN_CHECK_THRESHOLD == 0

if __name__ == '__main__':
    sample_values = [15, -4, 7, 8, -10, 3, 6, 9]
    results = {value: is_even(value) for value in sample_values}
    print(results)