START_VALUE = 10
STEP_VALUE = 5
COUNT_VALUE = 3

def count_generator():
    current = START_VALUE
    for _ in range(COUNT_VALUE):
        yield current
        current += STEP_VALUE

if __name__ == '__main__':
    gen = count_generator()
    result = next(gen)
    print(result)