def calculate_list_sum(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numeric.")
    return sum(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(calculate_list_sum(list1))
    
    list2 = [10.5, 20.5, 30.0]
    print(calculate_list_sum(list2))
    
    list3 = [-1, 5, -3, 10]
    print(calculate_list_sum(list3))