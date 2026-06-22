MAX_VALUE_NOT_FOUND = None

def find_largest(numbers):
    return max(numbers) if numbers else MAX_VALUE_NOT_FOUND

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_largest(sample_values))
    empty_list = []
    print(find_largest(empty_list))