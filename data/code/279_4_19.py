MUTIPLIER = 2

def cycle_and_double(numbers):
    for number in numbers:
        print(number * MUTIPLIER)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    cycle_and_double(sample_values)