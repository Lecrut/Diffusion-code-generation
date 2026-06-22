import statistics

def compute_mean(numbers):
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_data = [2.5, 3.5, 4.5, 5.5, 6.5]
    result = compute_mean(sample_data)
    print(result)