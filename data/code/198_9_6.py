class SmallestIntegerStringFinder:
    @staticmethod
    def find_smallest(strings):
        return min(strings, key=int)

if __name__ == '__main__':
    sample_strings = ["3", "15", "2", "9"]
    result = SmallestIntegerStringFinder.find_smallest(sample_strings)
    print(result)