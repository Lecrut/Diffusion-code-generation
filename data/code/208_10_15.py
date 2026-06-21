import statistics

def validate_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")

def calculate_mean(numbers):
    validate_numbers(numbers)
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    list3 = [-10, 20, 30]
    
    mean1 = calculate_mean(list1)
    mean2 = calculate_mean(list2)
    mean_empty = calculate_mean(empty_list)
    mean3 = calculate_mean(list3)
    
    print(f"Mean of {list1}: {mean1}")
    print(f"Mean of {list2}: {mean2}")
    print(f"Mean of {empty_list}: {mean_empty}")
    print(f"Mean of {list3}: {mean3}")