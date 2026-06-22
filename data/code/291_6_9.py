class MeasureComparer:
    def __init__(self, nanometers, micrometers):
        self.nanometers = nanometers
        self.micrometers = micrometers

    def compare(self):
        if self.nanometers < self.micrometers * 1000:
            return f"{self.nanometers} nm"
        else:
            return f"{self.micrometers} um"

if __name__ == '__main__':
    comparer = MeasureComparer(500, 2)
    print(comparer.compare())