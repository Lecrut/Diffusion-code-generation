def validate_input(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements must be integers")

def sort_list(data):
    return sorted(data)

if __name__ == '__main__':
    numbers = [5, 2, 8, 1, 9, 3]
    validate_input(numbers)
    sorted_numbers = sort_list(numbers)
    print(sorted_numbers)