POSITIVE_THRESHOLD = 0

def is_positive(x):
    return x > POSITIVE_THRESHOLD

if __name__ == '__main__':
    print(is_positive(15))
    print(is_positive(-7))
    print(is_positive(0))