import statistics

def calculate_average(numbers):
    if not numbers:
        return 0
    try:
        return statistics.mean(numbers)
    except TypeError as e:
        raise ValueError("Input must be a list of numbers") from e

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    invalid_input = ['a', 'b', 'c']
    
    print(f"Average of {list1}: {calculate_average(list1)}")
    print(f"Average of {list2}: {calculate_average(list2)}")
    print(f"Average of {empty_list}: {calculate_average(empty_list)}")
    try:
        print(f"Average of {invalid_input}: {calculate_average(invalid_input)}")
    except ValueError as e:
        print(e)