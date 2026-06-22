class VolumeComparator:
    VOLUME_1 = 50.0
    VOLUME_2 = 75.0

    @staticmethod
    def compare_volumes(volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers")
        if volume1 > volume2:
            return "Volume 1 is larger"
        elif volume1 < volume2:
            return "Volume 2 is larger"
        else:
            return "Volumes are equal"

if __name__ == '__main__':
    try:
        result = VolumeComparator.compare_volumes(VolumeComparator.VOLUME_1, VolumeComparator.VOLUME_2)
        print(result)
    except ValueError as e:
        print(e)