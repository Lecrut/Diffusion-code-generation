class VolumeComparator:
    def compare(self, volume1, volume2):
        comparison_result = 0
        difference = volume1 - volume2
        if volume1 > volume2:
            comparison_result = 1
        elif volume1 < volume2:
            comparison_result = -1
        else:
            comparison_result = 0
        return (comparison_result, difference)
if __name__ == '__main__':
    comparator = VolumeComparator()
    v1 = 100
    v2 = 150
    result1 = comparator.compare(v1, v2)
    print(f"Comparing {v1} and {v2}: {result1}")
    v3 = 200
    v4 = 200
    result2 = comparator.compare(v3, v4)
    print(f"Comparing {v3} and {v4}: {result2}")
    v5 = 50
    v6 = 25
    result3 = comparator.compare(v5, v6)
    print(f"Comparing {v5} and {v6}: {result3}")