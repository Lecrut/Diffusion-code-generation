class VolumeComparator:
    COMPARISON_THRESHOLD = 1e-9

    def compare(self, volume1, volume2):
        if abs(volume1 - volume2) < self.COMPARISON_THRESHOLD:
            comparison_result = "equal"
        elif volume1 > volume2:
            comparison_result = "volume1 is greater"
        else:
            comparison_result = "volume2 is greater"
        difference = abs(volume1 - volume2)
        return (comparison_result, difference)

if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(150.0, 150.000000001)
    print(result)