import random

def find_median(numbers):
    numbers.sort()
    length = len(numbers)
    middle_index = length // 2
    
    if length % 2 == 0:
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2.0
    else:
        return numbers[middle_index]

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000) for _ in range(100)]
    median_value = find_median(sample_data)
    print(median_value)