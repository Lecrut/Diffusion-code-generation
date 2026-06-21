class MinMaxTracker:
    def __init__(self):
        self.min_val = None
        self.max_val = None

    def add_number(self, number):
        if self.min_val is None or number < self.min_val:
            self.min_val = number
        if self.max_val is None or number > self.max_val:
            self.max_val = number

    def get_min(self):
        return self.min_val

    def get_max(self):
        return self.max_val

if __name__ == '__main__':
    tracker = MinMaxTracker()
    for number in [10, 5, 20, 3, 15, 25]:
        tracker.add_number(number)
    print("Current minimum:", tracker.get_min())
    print("Current maximum:", tracker.get_max())