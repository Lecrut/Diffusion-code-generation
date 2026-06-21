class RunningMinMax:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.min_val = float('inf')
        self.max_val = float('-inf')

    def next_min_max(self):
        try:
            value = next(self.iterable)
            if value < self.min_val:
                self.min_val = value
            if value > self.max_val:
                self.max_val = value
            return (self.min_val, self.max_val)
        except StopIteration:
            raise StopIteration("No more elements in the iterable")

if __name__ == '__main__':
    data = [15, 3, 8, 22, 1]
    rmm = RunningMinMax(data)
    print(f"First Min: {rmm.next_min_max()[0]}, First Max: {rmm.next_min_max()[1]}")
    print(f"Second Min: {rmm.next_min_max()[0]}, Second Max: {rmm.next_min_max()[1]}")
    print(f"Third Min: {rmm.next_min_max()[0]}, Third Max: {rmm.next_min_max()[1]}")