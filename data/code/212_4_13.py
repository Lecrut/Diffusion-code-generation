class NumberTracker:
    def __init__(self):
        self.min_value = None
        self.max_value = None

    def add_number(self, number):
        if self.min_value is None or number < self.min_value:
            self.min_value = number
        if self.max_value is None or number > self.max_value:
            self.max_value = number

    def get_min(self):
        return self.min_value

    def get_max(self):
        return self.max_value

if __name__ == '__main__':
    tracker = NumberTracker()
    numbers = [5, 3, 9, 1, 7]
    for num in numbers:
        tracker.add_number(num)
    print("Current Min:", tracker.get_min())
    print("Current Max:", tracker.get_max())