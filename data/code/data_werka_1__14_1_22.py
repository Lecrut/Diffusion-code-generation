class VolumeComparator:
    def compare(self, volume1, volume2):
        if volume1 > volume2:
            comparison_result = "volume1 is greater"
        elif volume1 < volume2:
            comparison_result = "volume2 is greater"
        else:
            comparison_result = "volumes are equal"
        
        difference = abs(volume1 - volume2)
        return (comparison_result, difference)

if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(100, 200)
    print(result)