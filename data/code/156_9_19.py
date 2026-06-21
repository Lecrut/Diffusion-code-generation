def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return None
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        return None

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [],
        ["a", "b", "c"],
        [10, 20, "error"]
    ]
    
    for lst in sample_lists:
        result = calculate_average(lst)
        print(f"Average of {lst}: {result}")