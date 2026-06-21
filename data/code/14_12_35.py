class VolumeComparator:
    def __init__(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        self.volume1 = volume1
        self.volume2 = volume2

    def compare(self):
        if self.volume1 > self.volume2:
            return "First volume is greater than the second."
        elif self.volume1 < self.volume2:
            return "First volume is less than the second."
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    try:
        comparator = VolumeComparator(4.5678, 3.14159)
        result = comparator.compare()
        print(result)
    except ValueError as e:
        print(e)