class VolumeComparator:

    def compare(self, volume1, volume2):
        if isinstance(volume1, (int, float)) and isinstance(volume2, (int, float)):
            comparison_result = 'greater' if volume1 > volume2 else 'less' if volume1 < volume2 else 'equal'
            difference = abs(volume1 - volume2)
            return (comparison_result, difference)
        else:
            raise ValueError('Both volumes must be numbers')
if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(10, 5)
    print(result)
    result = comparator.compare(3.5, 4.2)
    print(result)
    result = comparator.compare(7, 7)
    print(result)