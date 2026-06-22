class VolumeComparer:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def compare(self):
        if not isinstance(self.volume1, (int, float)) or not isinstance(self.volume2, (int, float)):
            raise ValueError("Both volumes must be numbers")
        
        if self.volume1 > self.volume2:
            return "Volume 1 is larger"
        elif self.volume1 < self.volume2:
            return "Volume 2 is larger"
        else:
            return "Volumes are equal"

if __name__ == '__main__':
    volume1 = 100.0
    volume2 = 50.0
    comparer = VolumeComparer(volume1, volume2)
    try:
        result = comparer.compare()
        print(result)
    except ValueError as e:
        print(e)