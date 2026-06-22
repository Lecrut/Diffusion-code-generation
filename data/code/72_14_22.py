class ArrayComparator:
    def __init__(self, first_array, second_array):
        if not isinstance(first_array, (list, tuple)):
            raise ValueError("first_array must be a list or tuple")
        if not isinstance(second_array, (list, tuple)):
            raise ValueError("second_array must be a list or tuple")
        self.first = list(first_array)
        self.second = list(second_array)

    def count_matches_at_positions(self, positions):
        if not isinstance(positions, (list, tuple)):
            raise ValueError("positions must be a list or tuple")
        if not positions:
            raise ValueError("positions cannot be empty")
        
        count = 0
        for pos in positions:
            if not isinstance(pos, int):
                raise ValueError("All positions must be integers")
            if pos < 0 or pos >= len(self.first) or pos < 0 or pos >= len(self.second):
                raise IndexError(f"Position {pos} is out of bounds for one or both arrays")
            if self.first[pos] == self.second[pos]:
                count += 1
        return count

if __name__ == '__main__':
    data_x = [5, 15, 25, 35, 45]
    data_y = [5, 16, 25, 36, 45]
    target_positions = [0, 2, 4]
    
    comparator = ArrayComparator(data_x, data_y)
    match_count = comparator.count_matches_at_positions(target_positions)
    
    print(match_count)