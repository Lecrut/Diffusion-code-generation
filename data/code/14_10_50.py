class VolumeComparator:
    VOLUME_1 = 600
    VOLUME_2 = 450

    @staticmethod
    def compare():
        if VolumeComparator.VOLUME_1 > VolumeComparator.VOLUME_2:
            return f"Volume 1 ({VolumeComparator.VOLUME_1}) is greater than Volume 2 ({VolumeComparator.VOLUME_2})."
        elif VolumeComparator.VOLUME_1 < VolumeComparator.VOLUME_2:
            return f"Volume 2 ({VolumeComparator.VOLUME_2}) is greater than Volume 1 ({VolumeComparator.VOLUME_1})."
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    result = VolumeComparator.compare()
    print(result)