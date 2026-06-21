class VolumeComparator:
    def compare(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers")
        
        difference = abs(volume1 - volume2)
        if volume1 > volume2:
            comparison_result = "volume1 is greater"
        elif volume1 < volume2:
            comparison_result = "volume2 is greater"
        else:
            comparison_result = "both volumes are equal"
        
        return (comparison_result, difference)

if __name__ == '__main__':
    comparator = VolumeComparator()
    result = comparator.compare(300.5, 200)
    print(result)