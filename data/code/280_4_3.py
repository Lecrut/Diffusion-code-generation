def print_squares():
    for i in range(1, 21):
        print(i ** 2)
if __name__ == '__main__':
    try:
        repetitions = 20
        if repetitions != 20:
            raise ValueError('Repetitions must be exactly 20.')
        for _ in range(repetitions):
            print_squares()
    except Exception as e:
        print(f'An error occurred: {e}')