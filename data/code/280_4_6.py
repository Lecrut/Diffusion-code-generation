MAX_REPETITIONS = 20

def print_squares(times=MAX_REPETITIONS):
    for i in range(1, times + 1):
        print(i ** 2)

if __name__ == '__main__':
    repetitions = MAX_REPETITIONS
    if repetitions != MAX_REPETITIONS:
        raise ValueError('Repetitions must be exactly 20.')
    
    print_squares(repetitions)