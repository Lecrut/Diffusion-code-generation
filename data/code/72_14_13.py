class ArrayComparator:
    def __init__(self, array_one, array_two):
        if not isinstance(array_one, (list, tuple)):
            raise ValueError("array_one must be a list or tuple")
        if not isinstance(array_two, (list, tuple)):
            raise ValueError("array_two must be a list or tuple")
        self._arr1 = array_one
        self._arr2 = array_two

    def count_matches_at_positions(self, positions):
        if not isinstance(positions, (list, tuple)):
            raise ValueError("positions must be a list or tuple")
        
        count = 0
        len1 = len(self._arr1)
        len2 = len(self._arr2)
        
        for pos in positions:
            if not isinstance(pos, int):
                raise ValueError("positions must contain integers")
            if pos < 0 or pos >= len1 or pos >= len2:
                continue
            if self._arr1[pos] == self._arr2[pos]:
                count += 1
        return count

if __name__ == '__main__':
    data_x = [5, 10, 15, 20, 25]
    data_y = [5, 12, 15, 22, 25]
    check_points = [0, 1, 2, 3, 4]
    
    comparator = ArrayComparator(data_x, data_y)
    result = comparator.count_matches_at_positions(check_points)
    print(result)