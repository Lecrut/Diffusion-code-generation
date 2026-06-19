class VolumeComparator:
    def compare(self, volume1, volume2):
        if volume1 > volume2:
            comparison_result = "Volume 1 is greater"
        elif volume1 < volume2:
            comparison_result = "Volume 2 is greater"
        else:
            comparison_result = "Both volumes are equal"
        
        difference = abs(volume1 - volume2)
        return (comparison_result, difference)

if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(500, 300)
    print(result)