import random
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [10, 25, 32, 48, 15]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)