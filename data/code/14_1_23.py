class VolumeComparator:
    def compare(self, volume1, volume2):
        comparison_result = "equal" if volume1 == volume2 else ("greater" if volume1 > volume2 else "lesser")
        difference = abs(volume1 - volume2)
        return (comparison_result, difference)

if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(100, 200)
    print(result)