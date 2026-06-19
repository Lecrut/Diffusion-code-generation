class ArrayComparator:
    ADJACENCY_STEP = 1

    @staticmethod
    def compare_elements(first, second):
        return (first, second)

    def check_adjacencies(self, numbers):
        result = []
        for i in range(len(numbers) - self.ADJACENCY_STEP):
            comparison = self.compare_elements(numbers[i], numbers[i + self.ADJACENCY_STEP])
            result.append(comparison)
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_values = [4, 7, 1, 9, 3]
    print(comparator.check_adjacencies(sample_values))