class AdjacentPairChecker:
    def __init__(self, arr):
        if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
            raise ValueError("Input must be a list of integers.")
        self.arr = arr

    def find_greater_indices(self):
        indices = []
        for i in range(len(self.arr) - 1):
            if self.arr[i + 1] > self.arr[i]:
                indices.append(i)
        return indices

if __name__ == '__main__':
    sample_array = [10, 20, 30, 25, 40, 50, 60]
    checker = AdjacentPairChecker(sample_array)
    result = checker.find_greater_indices()
    print(result)