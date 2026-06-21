import statistics

def compute_average(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    numbers = [15, 25, 35, 45, 55]
    average = compute_average(numbers)
    print(f"Average of {numbers}: {average}")