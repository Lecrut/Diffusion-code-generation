class MaxFinder:
    @staticmethod
    def find_largest(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return max(data, key=lambda x: x)

if __name__ == '__main__':
    sample_list = [-5, -10, -2, -8, -1]
    result = MaxFinder.find_largest(sample_list)
    print(result)