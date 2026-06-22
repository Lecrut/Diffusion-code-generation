class ArrayComparator:
    def check_adjacencies(self, numbers):
        if len(numbers) < 2:
            return []
        result = [(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1)]
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_values = [4, 8, 15, 16, 23, 42]
    print(comparator.check_adjacencies(sample_values))