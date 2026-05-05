def compare_successors(arr):
    n = len(arr)
    if n < 2:
        return
    for i in range(n - 1):
        if arr[i] < arr[i+1]:
            print(f"Comparison at index {i}: {arr[i]} < {arr[i+1]}")
        elif arr[i] > arr[i+1]:
            print(f"Comparison at index {i}: {arr[i]} > {arr[i+1]}")
        else:
            print(f"Comparison at index {i}: {arr[i]} == {arr[i+1]}")
if __name__ == '__main__':
    array1 = [1, 5, 2, 8, 3]
    print("--- Testing Array 1 ---")
    compare_successors(array1)
    array2 = [10, 10, 10, 5, 1]
    print("\n--- Testing Array 2 ---")
    compare_successors(array2)
    array3 = [42]
    print("\n--- Testing Array 3 (Edge Case: Single Element) ---")
    compare_successors(array3)
    array4 = []
    print("\n--- Testing Array 4 (Edge Case: Empty Array) ---")
    compare_successors(array4)
    array5 = [5, 5]
    print("\n--- Testing Array 5 (Equal Elements) ---")
    compare_successors(array5)