POSITIVE_THRESHOLD = 0
NEGATIVE_THRESHOLD = 0

def classify_number(num):
    if num > POSITIVE_THRESHOLD:
        return 'Positive'
    elif num < NEGATIVE_THRESHOLD:
        return 'Negative'
    else:
        return 'Zero'
if __name__ == '__main__':
    print(classify_number(12))
    print(classify_number(-8))
    print(classify_number(0))