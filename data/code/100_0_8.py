def classify_number(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

if __name__ == '__main__':
    print(classify_number(3))
    print(classify_number(-2))
    print(classify_number(0))