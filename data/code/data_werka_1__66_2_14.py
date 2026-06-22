class ArrayComparator:
    def check_adjacencies(self, numbers):
        if not numbers or len(numbers) < 2:
            return []
        
        comparisons = [(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1)]
        return comparisons

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_values = [4, 7, 1, 9, 2]
    print(comparator.check_adjacencies(sample_values))