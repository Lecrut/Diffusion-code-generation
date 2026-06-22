def calculate_square(number):
    return number ** 2

def repeat_and_print_squares(times):
    for i in range(1, times + 1):
        square = calculate_square(i)
        print(square)

if __name__ == '__main__':
    sample_repetitions = 20
    repeat_and_print_squares(sample_repetitions)