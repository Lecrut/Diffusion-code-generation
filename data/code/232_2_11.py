import itertools

NUMBERS_TO_PRINT = 20
START_NUMBER = 1

def print_sequence(count=NUMBERS_TO_PRINT, start=START_NUMBER):
    for number in itertools.count(start=start):
        if number > count:
            break
        print(number)

if __name__ == '__main__':
    print_sequence()