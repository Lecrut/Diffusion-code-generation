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
    comparator.compare(150.75, 150.75)
    comparator.compare(300.0, 100.5)
    comparator.compare(55.2, 100.0)