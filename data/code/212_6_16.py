class RunningMinMax:
    def __init__(self):
        self.min_val = float('inf')
        self.max_val = float('-inf')

    def update(self, value):
        if value < self.min_val:
            self.min_val = value
        if value > self.max_val:
            self.max_val = value

    def get_min_max(self):
        return (self.min_val, self.max_val)

def running_min_max(iterable):
    rmm = RunningMinMax()
    for value in iterable:
        rmm.update(value)
        yield rmm.get_min_max()

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    rmm_instance = RunningMinMax()
    for min_val, max_val in running_min_max(sample_data):
        print(f"Min: {min_val}, Max: {max_val}")