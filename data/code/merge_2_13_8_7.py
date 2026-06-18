class RunningMaxTracker:
    def __init__(self):
        self.current_max = float('-inf')
    def update(self, value):
        if value > self.current_max:
            self.current_max = value
    def get_current_max(self):
        return self.current_max
def process_sequence(sequence):
    tracker = RunningMaxTracker()
    for item in sequence:
        tracker.update(item)
    return tracker.get_current_max()
if __name__ == '__main__':
    sample_data = [3, 7, 2, 9, 1, 5]
    result = process_sequence(sample_data)
    print(result)