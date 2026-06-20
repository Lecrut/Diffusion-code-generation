NUMBER_STATUS = {
    'POSITIVE': 'Positive',
    'NEGATIVE': 'Negative',
    'ZERO': 'Zero'
}

def check_number(num):
    if num > 0:
        return NUMBER_STATUS['POSITIVE']
    elif num < 0:
        return NUMBER_STATUS['NEGATIVE']
    else:
        return NUMBER_STATUS['ZERO']

if __name__ == '__main__':
    print(check_number(5))
    print(check_number(-3))
    print(check_number(0))