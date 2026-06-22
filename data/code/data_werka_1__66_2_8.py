class ArrayComparator:
    def check_adjacencies(self, numbers):
        adjacencies = []
        for i in range(len(numbers) - 1):
            adjacencies.append((numbers[i], numbers[i + 1]))
        return adjacencies

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_numbers = [4, 7, 1, 9, 3]
    result = comparator.check_adjacencies(sample_numbers)
    print(result)