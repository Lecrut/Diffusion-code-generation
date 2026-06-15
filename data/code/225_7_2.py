class ValueStore:
    def __init__(self, values):
        self.values = values
    def get_min(self):
        return min(self.values)
    def get_max(self):
        return max(self.values)
    def get_range(self):
        return self.get_max() - self.get_min()
if __name__ == '__main__':
    sample_data = [10, 5, 20, 15, 3]
    store = ValueStore(sample_data)
    print(f"Values: {sample_data}")
    print(f"Minimum value: {store.get_min()}")
    print(f"Maximum value: {store.get_max()}")
    print(f"Range: {store.get_range()}")