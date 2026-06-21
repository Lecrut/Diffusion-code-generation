MAX_VALUE = float('-inf')

def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = MAX_VALUE
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_lists = [
        [3, 1, 4, 1, 5, 9, 2],
        [-10, -5, -20, -1],
        [7],
        []
    ]
    
    for i, list_ in enumerate(sample_lists):
        try:
            print(f"Largest in sample_list{i+1}: {find_largest(list_)}")
        except ValueError as e:
            print(e)