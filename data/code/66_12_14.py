class ArrayProcessor:
    def __init__(self, arr):
        self.arr = arr

    def validate_input(self):
        if not isinstance(self.arr, list) or not all(isinstance(x, (int, float)) for x in self.arr):
            raise ValueError("Input must be a list of numbers.")

    def compare_adjacent_pairs(self):
        self.validate_input()
        result = []
        n = len(self.arr)
        for i in range(n - 1):
            result.append(max(self.arr[i], self.arr[i + 1]))
        return result

if __name__ == '__main__':
    sample_array1 = [3, 1, 4, 1, 5, 9]
    sample_array2 = [10, 20, 30, 40, 50]
    sample_array3 = [5, 4, 3, 2, 1]
    
    processor1 = ArrayProcessor(sample_array1)
    processor2 = ArrayProcessor(sample_array2)
    processor3 = ArrayProcessor(sample_array3)
    
    result1 = processor1.compare_adjacent_pairs()
    result2 = processor2.compare_adjacent_pairs()
    result3 = processor3.compare_adjacent_pairs()
    
    print("Result for sample_array1:", result1)
    print("Result for sample_array2:", result2)
    print("Result for sample_array3:", result3)