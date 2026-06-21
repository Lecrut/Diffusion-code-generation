ODD_THRESHOLD = 2

def is_odd(num):
    return num % ODD_THRESHOLD != 0

if __name__ == '__main__':
    sample_values = [10, 15, 20, 25]
    results = {num: is_odd(num) for num in sample_values}
    print(results)