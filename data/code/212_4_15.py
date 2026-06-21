class MinMaxTracker:
    def __init__(self):
        self.current_min = None
        self.current_max = None

    def add_number(self, number):
        if self.current_min is None or number < self.current_min:
            self.current_min = number
        if self.current_max is None or number > self.current_max:
            self.current_max = number

    def get_current_min(self):
        return self.current_min

    def get_current_max(self):
        return self.current_max

if __name__ == '__main__':
    tracker = MinMaxTracker()
    numbers = [10, 5, 20, 3, 15, 25]
    for number in numbers:
        tracker.add_number(number)
        print(f"Current min: {tracker.get_current_min()}, Current max: {tracker.get_current_max()}")