class ArrayComparator:
    COMPARISON_LESS = "<"
    COMPARISON_GREATER = ">"
    COMPARISON_EQUAL = "=="

    @staticmethod
    def compare_elements(arr):
        n = len(arr)
        if n < 2:
            return
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                print(f"Comparison at index {i}: {arr[i]} {ArrayComparator.COMPARISON_LESS} {arr[i + 1]}")
            elif arr[i] > arr[i + 1]:
                print(f"Comparison at index {i}: {arr[i]} {ArrayComparator.COMPARISON_GREATER} {arr[i + 1]}")
            else:
                print(f"Comparison at index {i}: {arr[i]} {ArrayComparator.COMPARISON_EQUAL} {arr[i + 1]}")

if __name__ == '__main__':
    array1 = [3, 1, 4, 1, 5]
    print("--- Testing Array 1 ---")
    ArrayComparator.compare_elements(array1)
    array2 = [9, 8, 7, 6, 5]
    print("\n--- Testing Array 2 ---")
    ArrayComparator.compare_elements(array2)