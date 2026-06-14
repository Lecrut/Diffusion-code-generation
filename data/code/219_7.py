class MaxTracker:
    def __init__(self):
        self._max_value = float('-inf')
    def insert(self, value):
        if value > self._max_value:
            self._max_value = value
    def get_max(self):
        return self._max_value
if __name__ == '__main__':
    tracker = MaxTracker()
    sample_values = [10, 5, 20, 3, 15]
    for value in sample_values:
        tracker.insert(value)
        print(f"Inserted {value}, Current Max: {tracker.get_max()}")