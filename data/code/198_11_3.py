def find_smallest(numbers):
    return min(numbers)
if __name__ == '__main__':
    data1 = [3, 1, 4, 1, 5, 9, 2]
    result1 = find_smallest(data1)
    print(f"The smallest element in {data1} is: {result1}")
    data2 = [-10, 0, 5, -3, 8]
    result2 = find_smallest(data2)
    print(f"The smallest element in {data2} is: {result2}")
    data3 = [42]
    result3 = find_smallest(data3)
    print(f"The smallest element in {data3} is: {result3}")
    data4 = [100, 50, 25]
    result4 = find_smallest(data4)
    print(f"The smallest element in {data4} is: {result4}")