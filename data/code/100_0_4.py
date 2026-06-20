def classify_number(num):
    if num > 0:
        return 'Positive'
    if num < 0:
        return 'Negative'
    return 'Zero'

if __name__ == '__main__':
    print(classify_number(4))
    print(classify_number(-7))
    print(classify_number(0))