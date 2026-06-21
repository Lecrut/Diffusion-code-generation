class MinMaxTracker:
    def __init__(self):
        self.current_min = None
        self.current_max = None

    def add_number(self, number):
        if self.current_min is None or number < self.current_min:
            self.current_min = number
        if self.current_max is None or number > self.current_max:
            self.current_max = number

    def get_min(self):
        return self.current_min

    def get_max(self):
        return self.current_max

if __name__ == '__main__':
    tracker = MinMaxTracker()
    sample_data = [7, 2, 15, 8, 3]
    for num in sample_data:
        tracker.add_number(num)
    print(f"Current min: {tracker.get_min()}, Current max: {tracker.get_max()}")