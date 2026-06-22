def repeat_action(times):
    if not isinstance(times, int) or times < 0:
        raise ValueError('Number of repetitions must be a non-negative integer')
    counter = 0
    while counter < times:
        print(f'Action performed {counter + 1} time(s)')
        counter += 1
if __name__ == '__main__':
    number_of_repeats = 100
    repeat_action(number_of_repeats)