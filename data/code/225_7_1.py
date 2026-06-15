class ValueStore:
    def __init__(self, values):
        self.values = values
    def get_minimum(self):
        return min(self.values)
    def get_maximum(self):
        return max(self.values)
    def get_range(self):
        return self.get_maximum() - self.get_minimum()
if __name__ == '__main__':
    sample_data = [10, 5, 20, 8, 15]
    store = ValueStore(sample_data)
    print(f"Values: {sample_data}")
    print(f"Minimum: {store.get_minimum()}")
    print(f"Maximum: {store.get_maximum()}")
    print(f"Range: {store.get_range()}")