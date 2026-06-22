class VolumeComparator:
    def compare(self, volume1, volume2):
        if volume1 > volume2:
            return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
        elif volume1 < volume2:
            return f"Volume 1 ({volume1}) is smaller than Volume 2 ({volume2})."
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    comparator = VolumeComparator()
    print(comparator.compare(500, 300))
    print(comparator.compare(200, 200))
    print(comparator.compare(750, 1000))