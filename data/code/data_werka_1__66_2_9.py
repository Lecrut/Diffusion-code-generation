class ArrayComparator:
    def check_adjacencies(self, numbers):
        result = []
        for i in range(len(numbers) - 1):
            result.append((numbers[i], numbers[i + 1]))
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_values = [1, 2, 3, 4, 5]
    print(comparator.check_adjacencies(sample_values))