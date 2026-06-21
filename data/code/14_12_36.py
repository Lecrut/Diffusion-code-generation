class VolumeComparison:
    def __init__(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        self.volume1 = volume1
        self.volume2 = volume2

    def is_greater(self):
        return self.volume1 > self.volume2

    def is_less(self):
        return self.volume1 < self.volume2

    def are_equal(self):
        return self.volume1 == self.volume2

if __name__ == '__main__':
    try:
        comparator = VolumeComparison(7.8901, 3.14159)
        print("First volume is greater than the second:", comparator.is_greater())
        print("First volume is less than the second:", comparator.is_less())
        print("Both volumes are equal:", comparator.are_equal())
    except ValueError as e:
        print(e)