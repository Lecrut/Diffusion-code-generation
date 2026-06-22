MIN_THRESHOLD = 1
MAX_THRESHOLD = 100

def validate_triplet(a, b, c):
    values = [a, b, c]
    for value in values:
        is_positive = value > MIN_THRESHOLD
        is_even = value % 2 == 0
        is_under_limit = value < MAX_THRESHOLD
        if not (is_positive and is_even and is_under_limit):
            return False
    return True

if __name__ == '__main__':
    result1 = validate_triplet(10, 20, 30)
    print(result1)
    result2 = validate_triplet(10, 21, 30)
    print(result2)
    result3 = validate_triplet(10, 20, 100)
    print(result3)
    result4 = validate_triplet(-10, 20, 30)
    print(result4)