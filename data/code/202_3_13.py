class MaxFinder:
    @staticmethod
    def find_max_value(data):
        if not data:
            raise ValueError("Input dictionary cannot be empty")
        return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 5, 'c': 2, 'd': 9, 'e': 3}
    try:
        max_value = MaxFinder.find_max_value(sample_dict)
        print(f"Max value in {sample_dict}: {max_value}")
    except ValueError as e:
        print(f"Error caught: {e}")