def check_number(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be an integer or float")
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

if __name__ == '__main__':
    print(check_number(5))
    print(check_number(-3))
    print(check_number(0))