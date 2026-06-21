class MaxFinder:
    def find_largest(self, data):
        return max(data, key=lambda x: x)

if __name__ == '__main__':
    finder = MaxFinder()
    sample_list = [-5, -10, -2, -8, -1]
    result = finder.find_largest(sample_list)
    print(result)