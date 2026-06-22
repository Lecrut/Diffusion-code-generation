def compare_successors(arr):
    if len(arr) < 2:
        return
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            print(f"Index {i}: {arr[i]} < {arr[i + 1]}")
        elif arr[i] > arr[i + 1]:
            print(f"Index {i}: {arr[i]} > {arr[i + 1]}")
        else:
            print(f"Index {i}: {arr[i]} == {arr[i + 1]}")

if __name__ == '__main__':
    test_array_1 = [3, 1, 4, 1, 5]
    print("--- Test Array 1 ---")
    compare_successors(test_array_1)
    
    test_array_2 = [9, 8, 7, 6, 5]
    print("\n--- Test Array 2 ---")
    compare_successors(test_array_2)