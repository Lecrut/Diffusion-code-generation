LOWER_THRESHOLD = 0
UPPER_THRESHOLD = 100

def is_within_range(number):
    return LOWER_THRESHOLD <= number <= UPPER_THRESHOLD

if __name__ == '__main__':
    print(is_within_range(50))
    print(is_within_range(150))
    print(is_within_range(-10))