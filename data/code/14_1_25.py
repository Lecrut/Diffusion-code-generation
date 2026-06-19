class VolumeComparator:

    def compare(self, volume1, volume2):
        comparison_result = None
        difference = 0
        if volume1 > volume2:
            comparison_result = 'volume1 is greater'
            difference = volume1 - volume2
        elif volume1 < volume2:
            comparison_result = 'volume2 is greater'
            difference = volume2 - volume1
        else:
            comparison_result = 'both volumes are equal'
        return (comparison_result, difference)
if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(50, 30)
    print(result)