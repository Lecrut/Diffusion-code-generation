from functools import reduce

class MaxFinder:
    @staticmethod
    def find_max(sequence):
        return reduce(lambda x, y: x if x > y else y, sequence)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Maximum value in the sequence:", MaxFinder.find_max(sample_data))