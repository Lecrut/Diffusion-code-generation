NUMBERS_START = 1
NUMBERS_END = 10

def cycle_range(start=NUMBERS_START, end=NUMBERS_END):
    for number in range(start, end + 1):
        print(number)

if __name__ == '__main__':
    cycle_range()