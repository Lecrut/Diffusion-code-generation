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
    vol_a = 100
    vol_b = 150
    result1 = comparator.compare(vol_a, vol_b)
    print(f"Comparing {vol_a} and {vol_b}: {result1}")
    vol_c = 200
    vol_d = 200
    result2 = comparator.compare(vol_c, vol_d)
    print(f"Comparing {vol_c} and {vol_d}: {result2}")
    vol_e = 50
    vol_f = 75
    result3 = comparator.compare(vol_e, vol_f)
    print(f"Comparing {vol_e} and {vol_f}: {result3}")