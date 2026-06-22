import statistics

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_data = [
        [1.0, 2.5, 3.7],
        [10.2, 20.4, 30.6, 40.8],
        [5.5],
        [],
        [1.5, 2.5]
    ]

    for data_set in sample_data:
        try:
            average = calculate_mean(data_set)
            print(average)
        except ValueError as e:
            print(e)