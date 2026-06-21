class MaxFinder:
    @staticmethod
    def find_max(data):
        return max(data)

if __name__ == '__main__':
    finder = MaxFinder()
    sample_values = [10, 5, 20, 8, 15], [-5, -1, -10, -3], [42], []
    for values in sample_values:
        print(f"The largest value in {values} is: {finder.find_max(values)}")