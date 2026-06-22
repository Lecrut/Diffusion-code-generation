class MaxFinder:
    MAX_INT = 2**63 - 1

    @staticmethod
    def find_max_element(data):
        max_val = MaxFinder.MAX_INT
        for value in data:
            if value > max_val:
                max_val = value
        return max_val

if __name__ == '__main__':
    sample_data = [i for i in range(10**7)]
    finder = MaxFinder()
    print(finder.find_max_element(sample_data))