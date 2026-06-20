POSITIVE_THRESHOLD = 0
NEGATIVE_THRESHOLD = 0

def check_number(num):
    if num > POSITIVE_THRESHOLD:
        return 'Positive'
    elif num < NEGATIVE_THRESHOLD:
        return 'Negative'
    else:
        return 'Zero'

if __name__ == '__main__':
    print(check_number(5))
    print(check_number(-3))
    print(check_number(0))