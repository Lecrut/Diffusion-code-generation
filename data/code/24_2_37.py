NEGATIVE_THRESHOLD = 0

def is_negative(x):
    return x < NEGATIVE_THRESHOLD
if __name__ == '__main__':
    print(is_negative(-10))
    print(is_negative(0))
    print(is_negative(5))