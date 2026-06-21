def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = {
        "list1": [3, 1, 4, 1, 5, 9, 2],
        "list2": [-10, 5, 0, -3, 12],
        "list3": [42],
        "list4": [7],
        "list5": []
    }
    
    for name, value in sample_values.items():
        try:
            print(f"Smallest in {name}: {find_smallest(value)}")
        except ValueError as e:
            print(e)