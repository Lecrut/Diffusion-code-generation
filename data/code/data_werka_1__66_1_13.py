def compare_successors(arr):
    n = len(arr)
    if n < 2:
        return
    for i in range(n - 1):
        current = arr[i]
        successor = arr[i + 1]
        if current < successor:
            print(f"Comparison at index {i}: {current} < {successor}")
        elif current > successor:
            print(f"Comparison at index {i}: {current} > {successor}")
        else:
            print(f"Comparison at index {i}: {current} == {successor}")

if __name__ == '__main__':
    array1 = [3, 1, 4, 1, 5]
    print("--- Array 1 ---")
    compare_successors(array1)
    array2 = [9, 8, 7, 6, 5]
    print("\n--- Array 2 ---")
    compare_successors(array2)