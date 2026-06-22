class VolumeComparator:
    VOLUME_1_LARGER = "The first volume is larger."
    VOLUME_2_LARGER = "The second volume is larger."
    EQUAL_VOLUMES = "Both volumes are equal."

    @staticmethod
    def compare_volumes(volume1, volume2):
        if volume1 > volume2:
            return VolumeComparator.VOLUME_1_LARGER
        elif volume1 < volume2:
            return VolumeComparator.VOLUME_2_LARGER
        else:
            return VolumeComparator.EQUAL_VOLUMES

if __name__ == '__main__':
    sample_volume1 = 7.5
    sample_volume2 = 7.5
    result = VolumeComparator.compare_volumes(sample_volume1, sample_volume2)
    print(result)