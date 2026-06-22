MAX_REPETITIONS = 20

def print_square(number):
    print(number ** 2)

if __name__ == '__main__':
    for i in range(1, MAX_REPETITIONS + 1):
        print_square(i)