class MaxFinder:
    @staticmethod
    def find_max(values):
        if not values:
            raise ValueError("Input iterable cannot be empty")
        return max(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(f"Maximum of {sample_values}: {MaxFinder.find_max(sample_values)}")