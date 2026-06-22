def validate_repetitions(times):
    if times != 20:
        raise ValueError('Repetitions must be exactly 20.')

def print_squares(times):
    for i in range(1, times + 1):
        print(i ** 2)

if __name__ == '__main__':
    try:
        repetitions = 20
        validate_repetitions(repetitions)
        print_squares(repetitions)
    except Exception as e:
        print(f'An error occurred: {e}')