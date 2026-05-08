def find_largest(numbers):
    return max(numbers)
if __name__ == '__main__':
    data1 = [1, 5, 2, 8, 3]
    data2 = [-10, -5, -20, -1]
    data3 = [42]
    data4 = [100, 50, 200, 10]
    print(f"Largest in {data1}: {find_largest(data1)}")
    print(f"Largest in {data2}: {find_largest(data2)}")
    print(f"Largest in {data3}: {find_largest(data3)}")
    print(f"Largest in {data4}: {find_largest(data4)}")