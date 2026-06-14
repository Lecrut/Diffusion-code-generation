class ValueStore:
    def __init__(self, values):
        self.values = values
    def find_minimum(self):
        return min(self.values)
    def find_maximum(self):
        return max(self.values)
    def find_range(self):
        return self.find_maximum() - self.find_minimum()
if __name__ == '__main__':
    sample_data = [15, 8, 22, 4, 30, 11]
    store = ValueStore(sample_data)
    print(f"Values: {sample_data}")
    print(f"Minimum value: {store.find_minimum()}")
    print(f"Maximum value: {store.find_maximum()}")
    print(f"Range: {store.find_range()}")