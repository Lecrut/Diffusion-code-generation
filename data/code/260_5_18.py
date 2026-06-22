class MaxTupleFinder:
    def find_max_tuple(self, tuple1, tuple2):
        return tuple(max(value1, value2) for value1, value2 in zip(tuple1, tuple2))

if __name__ == '__main__':
    finder = MaxTupleFinder()
    result = finder.find_max_tuple((1, 3, 5), (2, 2, 6))
    print(result)