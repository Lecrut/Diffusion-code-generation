def find_largest(numbers):
    return max(numbers)
if __name__ == '__main__':
    data1 = [10, 5, 20, 8]
    result1 = find_largest(data1)
    print(f"The largest element in {data1} is: {result1}")
    data2 = [-5, -1, -10, -3]
    result2 = find_largest(data2)
    print(f"The largest element in {data2} is: {result2}")
    data3 = [42]
    result3 = find_largest(data3)
    print(f"The largest element in {data3} is: {result3}")