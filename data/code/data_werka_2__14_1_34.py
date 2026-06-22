class VolumeComparator:

    def compare(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError('Both volumes must be numbers')
        comparison_result = 'equal' if volume1 == volume2 else 'unequal'
        difference = abs(volume1 - volume2)
        return (comparison_result, difference)
if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(100.5, 100.5)
    print(result)
    result = comparator.compare(200, 150)
    print(result)