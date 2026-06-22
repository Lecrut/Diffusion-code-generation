def print_square(number):
    return number ** 2

def repeat_action(times):
    if times != 20:
        raise ValueError('Repetitions must be exactly 20.')
    
    for _ in range(times):
        for i in range(1, 21):
            print(print_square(i))

if __name__ == '__main__':
    try:
        repetitions = 20
        repeat_action(repetitions)
    except Exception as e:
        print(f'An error occurred: {e}')