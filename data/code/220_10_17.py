import statistics

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_data = [
        [1.0, 2.0, 3.0],
        [10.5, 20.5, 30.5, 40.5],
        [5.0],
        [],
        [1.2, 1.2, 1.2, 1.2]
    ]
    
    for data_set in sample_data:
        try:
            avg = calculate_mean(data_set)
            print(avg)
        except ValueError as e:
            print(e)