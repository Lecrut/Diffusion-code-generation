class ArrayComparator:
    def check_adjacencies(self, numbers):
        if not isinstance(numbers, list) or len(numbers) < 2:
            return []
        
        result = []
        for i in range(len(numbers) - 1):
            comparison = (numbers[i], numbers[i + 1])
            result.append(comparison)
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_list = [4, 7, 1, 9, 2]
    comparison_results = comparator.check_adjacencies(sample_list)
    print(comparison_results)