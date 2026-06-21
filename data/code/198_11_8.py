def find_smallest(numbers):
    smallest = float('inf')
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    data1 = [3.5, 1.2, 4.8, 1.0, 5.6, 9.7, 2.1]
    result1 = find_smallest(data1)
    print(f"The smallest element in {data1} is: {result1}")
    
    data2 = [-10.3, 5.4, 0.8, -3.2, 8.9]
    result2 = find_smallest(data2)
    print(f"The smallest element in {data2} is: {result2}")
    
    data3 = [42.0]
    result3 = find_smallest(data3)
    print(f"The smallest element in {data3} is: {result3}")