class ArrayComparator:
    def check_adjacencies(self, numbers):
        if not numbers or len(numbers) < 2:
            return []
        
        result = [(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1)]
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_list = [4, 9, 1, 3, 7]
    comparison_results = comparator.check_adjacencies(sample_list)
    print(comparison_results)