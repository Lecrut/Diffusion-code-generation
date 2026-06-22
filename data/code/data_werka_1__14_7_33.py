class VolumeComparator:
    def compare(self, volume1, volume2):
        if volume1 > volume2:
            return "Volume 1 is greater than Volume 2."
        elif volume1 < volume2:
            return "Volume 1 is smaller than Volume 2."
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(500, 300)
    print(result)