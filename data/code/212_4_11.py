class MinMaxTracker:
    def __init__(self):
        self.current_min = None
        self.current_max = None

    def add_number(self, number):
        if self.current_min is None:
            self.current_min = number
            self.current_max = number
        else:
            if number < self.current_min:
                self.current_min = number
            if number > self.current_max:
                self.current_max = number

    def get_min(self):
        return self.current_min

    def get_max(self):
        return self.current_max

if __name__ == '__main__':
    tracker = MinMaxTracker()
    sample_data = [10, 5, 20, 3, 15, 25]
    for number in sample_data:
        tracker.add_number(number)
        print(f"Added {number}: min={tracker.get_min()}, max={tracker.get_max()}")