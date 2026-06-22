class VolumeComparator:
    @staticmethod
    def compare(volume1, volume2):
        if volume1 > volume2:
            return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
        elif volume1 < volume2:
            return f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1})."
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    VOLUME_A = 350
    VOLUME_B = 700
    result = VolumeComparator.compare(VOLUME_A, VOLUME_B)
    print(result)