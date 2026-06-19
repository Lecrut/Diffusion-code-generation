class ArrayComparator:
    def __init__(self, arr):
        self.arr = arr

    def compare_successors(self):
        n = len(self.arr)
        if n < 2:
            return
        for i in range(n - 1):
            if self.arr[i] < self.arr[i + 1]:
                print(f"Comparison at index {i}: {self.arr[i]} < {self.arr[i + 1]}")
            elif self.arr[i] > self.arr[i + 1]:
                print(f"Comparison at index {i}: {self.arr[i]} > {self.arr[i + 1]}")
            else:
                print(f"Comparison at index {i}: {self.arr[i]} == {self.arr[i + 1]}")

if __name__ == '__main__':
    array1 = [3, 1, 4, 1, 5, 9]
    comparator1 = ArrayComparator(array1)
    print("--- Testing Array 1 ---")
    comparator1.compare_successors()

    array2 = [7, 7, 7, 7]
    comparator2 = ArrayComparator(array2)
    print("\n--- Testing Array 2 ---")
    comparator2.compare_successors()