from functools import reduce

def find_maximum(numbers):
    return reduce(lambda current_max, number: max(current_max, number), numbers)

if __name__ == '__main__':
    sample_values = [7, 2, 9, 3, 5]
    print(find_maximum(sample_values))