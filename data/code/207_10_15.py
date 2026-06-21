MAX_VALUE = float('-inf')

def find_max_element(numbers):
    return max(numbers, default=MAX_VALUE)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(find_max_element(sample_values))