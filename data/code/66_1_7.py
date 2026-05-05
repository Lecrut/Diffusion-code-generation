def compare_successors(arr):
    n = len(arr)
    if n < 2:
        return
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            print(f"Comparison at index {i}: {arr[i]} > {arr[i+1]}")
        elif arr[i] < arr[i+1]:
            print(f"Comparison at index {i}: {arr[i]} < {arr[i+1]}")
        else:
            print(f"Comparison at index {i}: {arr[i]} == {arr[i+1]}")
if __name__ == '__main__':
    array1 = [1, 5, 2, 8, 3]
    print("--- Array 1 ---")
    compare_successors(array1)
    array2 = [10, 10, 10]
    print("\n--- Array 2 ---")
    compare_successors(array2)
    array3 = [5]
    print("\n--- Array 3 (Edge Case) ---")
    compare_successors(array3)
    array4 = []
    print("\n--- Array 4 (Edge Case) ---")
    compare_successors(array4)
    array5 = [10, 5, 20]
    print("\n--- Array 5 ---")
    compare_successors(array5)