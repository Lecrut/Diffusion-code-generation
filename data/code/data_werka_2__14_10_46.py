class VolumeComparer:
    VOLUME_1 = 300
    VOLUME_2 = 450

    @staticmethod
    def compare(volume1, volume2):
        if volume1 > volume2:
            return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
        elif volume1 < volume2:
            return f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1})."
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    comparer = VolumeComparer()
    result = comparer.compare(VolumeComparer.VOLUME_1, VolumeComparer.VOLUME_2)
    print(result)