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
    tracker.add_number(10)
    tracker.add_number(5)
    tracker.add_number(20)
    tracker.add_number(3)
    tracker.add_number(15)
    tracker.add_number(25)

    print("Current Min:", tracker.get_min())
    print("Current Max:", tracker.get_max())