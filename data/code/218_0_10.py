MINIMUM_THRESHOLD = 0

def find_minimum(numbers):
    return min(filter(lambda x: x >= MINIMUM_THRESHOLD, numbers))

if __name__ == '__main__':
    sample_values = [45, 12, 89, -3, 56, 7]
    print(find_minimum(sample_values))