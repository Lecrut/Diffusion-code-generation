ODD_MODULO = 2

def is_odd(num):
    return num % ODD_MODULO != 0

if __name__ == '__main__':
    SAMPLE_NUMBER = 17
    print(is_odd(SAMPLE_NUMBER))