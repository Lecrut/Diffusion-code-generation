class VolumeComparator:
    def __init__(self, volume1: float, volume2: float):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        self.volume1 = volume1
        self.volume2 = volume2

    def compare(self) -> str:
        if self.volume1 > self.volume2:
            return "Volume 1 is greater than Volume 2."
        elif self.volume1 < self.volume2:
            return "Volume 2 is greater than Volume 1."
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    comparator = VolumeComparator(50.8, 30.6)
    result1 = comparator.compare()
    print(result1)

    comparator2 = VolumeComparator(75.1, 48.2)
    result2 = comparator2.compare()
    print(result2)