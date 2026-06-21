EVEN_THRESHOLD = 2
ZERO_VALUE = 0

def even_zero_generator(start, end):
    for num in range(start, end + 1):
        if num % EVEN_THRESHOLD == 0:
            yield num == ZERO_VALUE

if __name__ == '__main__':
    START_VALUE = -10
    END_VALUE = 20
    for result in even_zero_generator(START_VALUE, END_VALUE):
        print(result)