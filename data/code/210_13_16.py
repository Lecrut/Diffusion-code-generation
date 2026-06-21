MAX_NUMBER = float('inf')
MIN_NUMBER = float('-inf')

def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(calculate_range(sample_numbers))