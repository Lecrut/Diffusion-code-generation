def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return max(numbers)
if __name__ == '__main__':
    data1 = [10, 5, 20, 15]
    data2 = [-5, -1, -10]
    data3 = [3.14, 2.71, 1.618]
    data4 = [42]
    data5 = []
    print(f"Largest in {data1}: {find_largest(data1)}")
    print(f"Largest in {data2}: {find_largest(data2)}")
    print(f"Largest in {data3}: {find_largest(data3)}")
    print(f"Largest in {data4}: {find_largest(data4)}")
    try:
        find_largest(data5)
    except ValueError as e:
        print(f"Error for {data5}: {e}")