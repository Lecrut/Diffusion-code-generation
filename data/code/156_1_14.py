def calculate_average(data):
    if not data:
        return None
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    
    avg1 = calculate_average(list1)
    print(f"Average of {list1}: {avg1}")
    
    avg2 = calculate_average(list2)
    print(f"Average of {list2}: {avg2}")
    
    avg3 = calculate_average(empty_list)
    print(f"Average of {empty_list}: {avg3}")