def find_smallest(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    data1 = [3, 1, 4, 1, 5, 9, 2]
    result1 = find_smallest(data1)
    print(f"The smallest element in {data1} is: {result1}")
    
    data2 = [-10, 5, 0, -3, 8]
    result2 = find_smallest(data2)
    print(f"The smallest element in {data2} is: {result2}")
    
    data3 = [42]
    result3 = find_smallest(data3)
    print(f"The smallest element in {data3} is: {result3}")