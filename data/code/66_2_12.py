class ArrayComparator:
    def check_adjacencies(self, numbers):
        result = []
        for i in range(len(numbers) - 1):
            comparison = (numbers[i], numbers[i + 1])
            result.append(comparison)
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_values = [4, 9, 15, 23, 42]
    print(comparator.check_adjacencies(sample_values))