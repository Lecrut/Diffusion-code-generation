ODD_THRESHOLD = 50

def find_odd_numbers(limit):
    return [num for num in range(1, limit + 1) if num % 2 != 0]

if __name__ == '__main__':
    sample_limit = ODD_THRESHOLD
    result = find_odd_numbers(sample_limit)
    print(result)