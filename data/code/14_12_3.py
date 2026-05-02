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
    comparator.compare(150.5, 120.0)
    comparator.compare(300, 300)
    comparator.compare(55.2, 60.1)