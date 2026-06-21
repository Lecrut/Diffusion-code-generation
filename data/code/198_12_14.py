class MinFinder:
    @staticmethod
    def find_smallest(numbers):
        if not numbers:
            return None
        return min(numbers)

if __name__ == '__main__':
    sample1 = [-5, 2]
    sample2 = [10, -8]
    sample3 = [1, 2, 3]
    sample4 = []

    print(MinFinder.find_smallest(sample1))
    print(MinFinder.find_smallest(sample2))
    print(MinFinder.find_smallest(sample3))
    print(MinFinder.find_smallest(sample4))