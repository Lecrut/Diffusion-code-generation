import statistics

NUMBERS = [10, 20, 30, 40, 50]

def calculate_average(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    print(f"Average of {NUMBERS}: {calculate_average(NUMBERS)}")