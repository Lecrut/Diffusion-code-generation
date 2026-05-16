def find_largest(numbers):
    return max(numbers)
if __name__ == '__main__':
    data1 = [10, 5, 20, 8, 15]
    data2 = [-5, -1, -10, -3]
    data3 = [42]
    data4 = [3.14, 2.71, 1.618]
    print(f"Largest in {data1}: {find_largest(data1)}")
    print(f"Largest in {data2}: {find_largest(data2)}")
    print(f"Largest in {data3}: {find_largest(data3)}")
    print(f"Largest in {data4}: {find_largest(data4)}")