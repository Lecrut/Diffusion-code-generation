ODD_CHECK = 2

def is_odd(n):
    return n % ODD_CHECK != 0

if __name__ == '__main__':
    sample_values = [10, 15, -7, 8, 0, -2]
    results = {value: is_odd(value) for value in sample_values}
    print(results)