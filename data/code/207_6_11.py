class MaxFinder:
    def __init__(self, generator):
        self.generator = generator

    def find_largest(self):
        largest = next(self.generator)
        for item in self.generator:
            if item > largest:
                largest = item
        return largest

if __name__ == '__main__':
    sample_generator = iter([1, 5, 2, 8, 3])
    finder = MaxFinder(sample_generator)
    print(finder.find_largest())