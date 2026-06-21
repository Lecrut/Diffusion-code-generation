THRESHOLD = 0

is_greater_than_threshold = lambda x, y: x > THRESHOLD and y > THRESHOLD

if __name__ == '__main__':
    print(is_greater_than_threshold(10, 5))
    print(is_greater_than_threshold(3, 7))