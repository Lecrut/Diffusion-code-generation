def compare_successors(arr):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input must be a list of integers.")
    
    n = len(arr)
    if n < 2:
        print("Array has fewer than two elements, no comparisons to make.")
        return
    
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            print(f"Comparison at index {i}: {arr[i]} < {arr[i + 1]}")
        elif arr[i] > arr[i + 1]:
            print(f"Comparison at index {i}: {arr[i]} > {arr[i + 1]}")
        else:
            print(f"Comparison at index {i}: {arr[i]} == {arr[i + 1]}")

if __name__ == '__main__':
    array1 = [3, 7, 2, 6, 4]
    print("--- Testing Array 1 ---")
    compare_successors(array1)
    
    array2 = [9, 9, 8, 8]
    print("\n--- Testing Array 2 ---")
    compare_successors(array2)
    
    array3 = [5]
    print("\n--- Testing Array 3 ---")
    compare_successors(array3)