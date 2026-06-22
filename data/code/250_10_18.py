import statistics

def calculate_average(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("Input must be a list of integers or floats")
    return statistics.mean(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    list3 = [-10, 20, 30]
    
    print(f"Average of {list1}: {calculate_average(list1)}")
    print(f"Average of {list2}: {calculate_average(list2)}")
    print(f"Average of {empty_list}: {calculate_average(empty_list)}")
    print(f"Average of {list3}: {calculate_average(list3)}")