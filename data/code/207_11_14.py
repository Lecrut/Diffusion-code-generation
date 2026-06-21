class MaxFinder:
    @staticmethod
    def find_maximum(iterable):
        if not iterable:
            raise ValueError("Input iterable cannot be empty")
        return max(iterable, key=lambda x: x)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    max_value = MaxFinder.find_maximum(sample_values)
    print(max_value)