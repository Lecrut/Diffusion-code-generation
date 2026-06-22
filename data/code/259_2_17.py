class MinMaxFinder:
    def find_min_max(self, data_tuple):
        if not data_tuple:
            return None, None
        minimum = maximum = data_tuple[0]
        for item in data_tuple:
            if self._is_smaller(item, minimum):
                minimum = item
            elif self._is_larger(item, maximum):
                maximum = item
        return minimum, maximum

    def _is_smaller(self, a, b):
        return not (a > b)

    def _is_larger(self, a, b):
        return not (b > a)

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data1 = (10, 5, 20, 8, 15)
    min1, max1 = finder.find_min_max(sample_data1)
    print(f"Data: {sample_data1}")
    print(f"Minimum: {min1}, Maximum: {max1}")

    sample_data2 = (-5, 100, 0, -50)
    min2, max2 = finder.find_min_max(sample_data2)
    print(f"Data: {sample_data2}")
    print(f"Minimum: {min2}, Maximum: {max2}")