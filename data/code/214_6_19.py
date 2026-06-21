class SmallestValueFinder:
    def __init__(self, generator):
        self.generator = generator

    def find_smallest(self):
        try:
            smallest = next(self.generator)
            for value in self.generator:
                if value < smallest:
                    smallest = value
            return smallest
        except StopIteration:
            return None

if __name__ == '__main__':
    sample_data = (10, 5, 2, 8, 1)
    finder = SmallestValueFinder(iter(sample_data))
    print(finder.find_smallest())