class MaxFinder:
    @staticmethod
    def find_maximum(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return max(data, key=lambda x: x)

if __name__ == '__main__':
    sample_list = [3, 15, 2, 88, 1, 42, 9]
    result = MaxFinder.find_maximum(sample_list)
    print(result)