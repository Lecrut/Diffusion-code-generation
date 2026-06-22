class VolumeComparator:
    def compare(self, volume1, volume2):
        if volume1 > volume2:
            return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
        if volume1 < volume2:
            return f"Volume 1 ({volume1}) is smaller than Volume 2 ({volume2})."
        return "Both volumes are equal."

if __name__ == '__main__':
    comparator = VolumeComparator()
    print(comparator.compare(75, 40))
    print(comparator.compare(60, 60))
    print(comparator.compare(120, 90))