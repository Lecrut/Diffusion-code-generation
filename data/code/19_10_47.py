POSITIVE_THRESHOLD = 0

def is_positive(number):
    return number > POSITIVE_THRESHOLD

if __name__ == '__main__':
    sample_values = [15, -3, 0, 8, -7]
    results = {value: is_positive(value) for value in sample_values}
    print(results)