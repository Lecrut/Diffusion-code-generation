class VolumeComparator:
    EQUAL = "equal"
    GREATER = "greater"
    LESSER = "lesser"

    @staticmethod
    def determine_comparison(volume1, volume2):
        if volume1 > volume2:
            return VolumeComparator.GREATER
        elif volume1 < volume2:
            return VolumeComparator.LESSER
        else:
            return VolumeComparator.EQUAL

    def compare(self, volume1, volume2):
        comparison_result = self.determine_comparison(volume1, volume2)
        difference = abs(volume1 - volume2)
        return (comparison_result, difference)

if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(300, 150)
    print(result)