class MinFinder:
    @staticmethod
    def find_minimum(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return min(data)

if __name__ == '__main__':
    sample_list = ['cherry', 'banana', 'apple']
    minimum_value = MinFinder.find_minimum(sample_list)
    print(minimum_value)