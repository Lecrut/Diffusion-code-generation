def validate_input(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements must be integers")

def sort_ascending(numbers):
    validate_input(numbers)
    return sorted(numbers)

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    sorted_list = sort_ascending(sample_list)
    print(sorted_list)