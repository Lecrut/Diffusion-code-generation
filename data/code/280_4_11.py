def print_squares(times):
    if times != 20:
        raise ValueError('Times must be exactly 20.')
    for i in range(1, 21):
        print(i ** 2)

if __name__ == '__main__':
    try:
        repetitions = 20
        print_squares(repetitions)
    except Exception as e:
        print(f'An error occurred: {e}')