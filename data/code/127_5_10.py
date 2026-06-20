ODD_NUMBERS_START = 1
ODD_NUMBERS_END = 10

def odd_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

if __name__ == '__main__':
    result = list(odd_generator(ODD_NUMBERS_START, ODD_NUMBERS_END))
    print(result)