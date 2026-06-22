def repeat_action(times):
    counter = 0
    while counter < times:
        counter += 1
if __name__ == '__main__':
    try:
        number_of_repeats = 100
        if not isinstance(number_of_repeats, int) or number_of_repeats <= 0:
            raise ValueError('Number of repeats must be a positive integer')
        repeat_action(number_of_repeats)
        print(f'Action repeated {number_of_repeats} times.')
    except ValueError as e:
        print(e)