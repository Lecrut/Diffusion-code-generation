class ArrayComparator:
    def check_adjacencies(self, numbers):
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list")
        
        result = []
        for i in range(len(numbers) - 1):
            comparison = (numbers[i], numbers[i + 1])
            result.append(comparison)
        
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_list = [4, 9, 1, 6, 2]
    try:
        comparison_results = comparator.check_adjacencies(sample_list)
        print(comparison_results)
    except ValueError as e:
        print(e)