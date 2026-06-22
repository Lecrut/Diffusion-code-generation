def compare_successors(arr):
    operations = {
        '<': lambda x, y: f"{x} < {y}",
        '>': lambda x, y: f"{x} > {y}",
        '==': lambda x, y: f"{x} == {y}"
    }
    
    n = len(arr)
    if n < 2:
        return
    
    for i in range(n - 1):
        result_key = '<' if arr[i] < arr[i+1] else '>' if arr[i] > arr[i+1] else '=='
        print(f"Comparison at index {i}: {operations[result_key](arr[i], arr[i+1])}")

if __name__ == '__main__':
    array1 = [3, 1, 4, 1, 5]
    print("--- Testing Array 1 ---")
    compare_successors(array1)
    
    array2 = [7, 8, 9]
    print("\n--- Testing Array 2 ---")
    compare_successors(array2)
    
    array3 = [5, 5, 5, 5]
    print("\n--- Testing Array 3 ---")
    compare_successors(array3)