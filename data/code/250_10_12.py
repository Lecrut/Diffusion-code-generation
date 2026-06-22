import statistics

def calculate_average(numbers):
    if not numbers:
        return 0
    return statistics.mean(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    list3 = [-10, 20, 30]
    
    avg1 = calculate_average(list1)
    avg2 = calculate_average(list2)
    avg_empty = calculate_average(empty_list)
    avg3 = calculate_average(list3)
    
    print(f"Average of {list1}: {avg1}")
    print(f"Average of {list2}: {avg2}")
    print(f"Average of {empty_list}: {avg_empty}")
    print(f"Average of {list3}: {avg3}")