class BoundaryInspector:
    def __init__(self, values):
        self.values = values

    def inspect_bounds(self):
        count = len(self.values)
        if count < 2:
            raise ValueError("Insufficient elements")
        first = self.values[0]
        last = self.values[-1]
        return first, last

if __name__ == '__main__':
    inspector = BoundaryInspector([42, 99, 15, 88])
    bounds = inspector.inspect_bounds()
    print(bounds)