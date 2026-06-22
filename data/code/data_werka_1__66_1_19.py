def compare_successors(arr):
    if len(arr) < 2:
        return
    for i in range(len(arr) - 1):
        current, successor = arr[i], arr[i + 1]
        if current < successor:
            print(f"Comparison at index {i}: {current} < {successor}")
        elif current > successor:
            print(f"Comparison at index {i}: {current} > {successor}")
        else:
            print(f"Comparison at index {i}: {current} == {successor}")

if __name__ == '__main__':
    test_array1 = [3, 1, 4, 1, 5]
    print("--- Testing Array 1 ---")
    compare_successors(test_array1)
    
    test_array2 = [7, 7, 7, 7]
    print("\n--- Testing Array 2 ---")
    compare_successors(test_array2)