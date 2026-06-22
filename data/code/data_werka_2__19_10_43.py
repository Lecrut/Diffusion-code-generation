POSITIVE_THRESHOLD = 0

def is_positive(number):
    return number > POSITIVE_THRESHOLD

if __name__ == '__main__':
    sample_values = [10, -5, 0, 3, -1]
    for value in sample_values:
        print(f"{value}: {is_positive(value)}")