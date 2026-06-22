NUM_REPETITIONS = 15

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == '__main__':
    for i in range(NUM_REPETITIONS):
        print(f"{i} is {check_even_odd(i)}")