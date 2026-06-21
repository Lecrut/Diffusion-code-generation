class VolumeComparator:
    VOLUME_1 = 85.2
    VOLUME_2 = 47.6

    @staticmethod
    def compare(volume1: float, volume2: float) -> str:
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        if volume1 > volume2:
            return "Volume 1 is greater than Volume 2."
        elif volume1 < volume2:
            return "Volume 2 is greater than Volume 1."
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    result = VolumeComparator.compare(VolumeComparator.VOLUME_1, VolumeComparator.VOLUME_2)
    print(result)