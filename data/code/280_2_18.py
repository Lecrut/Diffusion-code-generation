def repeat_action(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be a non-negative integer')
    counter = 0
    while counter < n:
        print(f'Action performed {counter + 1} times')
        counter += 1
if __name__ == '__main__':
    number_of_repeats = 100
    repeat_action(number_of_repeats)