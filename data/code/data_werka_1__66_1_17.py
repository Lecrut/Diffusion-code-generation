COMPARISON_THRESHOLD = 0

def compare_successors(arr):
    n = len(arr)
    if n < 2:
        return
    for i in range(n - 1):
        diff = arr[i] - arr[i + 1]
        if diff < COMPARISON_THRESHOLD:
            print(f"Comparison at index {i}: {arr[i]} < {arr[i+1]}")
        elif diff > COMPARISON_THRESHOLD:
            print(f"Comparison at index {i}: {arr[i]} > {arr[i+1]}")
        else:
            print(f"Comparison at index {i}: {arr[i]} == {arr[i+1]}")

if __name__ == '__main__':
    array1 = [3, 1, 4, 1, 5]
    print("--- Array 1 ---")
    compare_successors(array1)
    
    array2 = [7, 7, 7, 7]
    print("\n--- Array 2 ---")
    compare_successors(array2)