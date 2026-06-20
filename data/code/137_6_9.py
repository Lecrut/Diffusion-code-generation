def check_range():
    LOWER_THRESHOLD = 1
    UPPER_THRESHOLD = 10
    return LOWER_THRESHOLD <= 5 <= UPPER_THRESHOLD

if __name__ == '__main__':
    print(check_range())