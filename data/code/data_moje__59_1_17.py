BASE_NUMBER = 12345

def sum_digits(number):
    return sum(map(int, str(abs(number))))

if __name__ == '__main__':
    print(sum_digits(BASE_NUMBER))