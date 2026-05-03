class VolumeComparator:
    def compare(self, volume1, volume2):
        if volume1 > volume2:
            print(f"{volume1} is greater than {volume2}")
        elif volume1 < volume2:
            print(f"{volume1} is smaller than {volume2}")
        else:
            print(f"{volume1} is equal to {volume2}")
if __name__ == '__main__':
    comparator = VolumeComparator()
    v1 = 150.75
    v2 = 200.50
    comparator.compare(v1, v2)
    v3 = 42
    v4 = 42
    comparator.compare(v3, v4)
    v5 = 99.99
    v6 = 100.01
    comparator.compare(v5, v6)