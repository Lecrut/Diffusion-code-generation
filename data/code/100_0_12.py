def check_number(num):
    if num > 0:
        return 'Positive'
    if num < 0:
        return 'Negative'
    return 'Zero'

if __name__ == '__main__':
    print(check_number(5))
    print(check_number(-3))
    print(check_number(0))