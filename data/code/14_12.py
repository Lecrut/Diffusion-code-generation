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
    volume_a = 150.75
    volume_b = 200.50
    comparator.compare(volume_a, volume_b)
    volume_c = 42
    volume_d = 42
    comparator.compare(volume_c, volume_d)
    volume_e = 99.99
    volume_f = 100.01
    comparator.compare(volume_e, volume_f)