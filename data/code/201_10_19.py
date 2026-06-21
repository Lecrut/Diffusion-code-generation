import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [2, 4, 6, 8, 10]
    avg = calculate_average(sample_numbers)
    print(avg)