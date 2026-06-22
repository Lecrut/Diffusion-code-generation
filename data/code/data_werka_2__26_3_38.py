GREATER_THAN_THRESHOLD = 0

def check_greater(x, y):
    return int(x > y) > GREATER_THAN_THRESHOLD

if __name__ == '__main__':
    x = 15
    y = 7
    print(check_greater(x, y))