import statistics

def calculate_average(numbers):
    if not numbers:
        return 0
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3, 4, 5],
        [10.5, 20.5, 30.5],
        [],
        [-10, 20, 30]
    ]
    for values in sample_values:
        print(f"Average of {values}: {calculate_average(values)}")