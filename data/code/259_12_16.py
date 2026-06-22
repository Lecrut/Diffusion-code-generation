class ValueExtremes:
    def __init__(self):
        self.data = []

    def store_list(self, data_list):
        if not isinstance(data_list, list) or not all(isinstance(x, int) for x in data_list):
            raise ValueError("Input must be a list of integers")
        self.data = data_list

    def find_min(self):
        if not self.data:
            return None
        return min(self.data)

    def find_max(self):
        if not self.data:
            return None
        return max(self.data)

if __name__ == '__main__':
    extremes = ValueExtremes()
    sample_data = [10, 5, 22, 8, 30, 1]
    extremes.store_list(sample_data)
    minimum_val = extremes.find_min()
    maximum_val = extremes.find_max()
    print(f"Data: {sample_data}")
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")