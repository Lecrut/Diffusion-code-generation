class ArrayIndexComparator:
    def __init__(self, array_a, array_b):
        self.array_a = array_a
        self.array_b = array_b

    def count_matches_at(self, indices):
        match_count = 0
        for idx in indices:
            if idx < len(self.array_a) and idx < len(self.array_b):
                if self.array_a[idx] == self.array_b[idx]:
                    match_count += 1
        return match_count

    def get_matching_values_at(self, indices):
        matching_values = []
        for idx in indices:
            if idx < len(self.array_a) and idx < len(self.array_b):
                if self.array_a[idx] == self.array_b[idx]:
                    matching_values.append(self.array_a[idx])
        return matching_values

if __name__ == '__main__':
    data_set_one = [1, 2, 3, 4, 5]
    data_set_two = [1, 5, 3, 8, 9]
    check_positions = [0, 2, 4]

    comparator = ArrayIndexComparator(data_set_one, data_set_two)
    count_result = comparator.count_matches_at(check_positions)
    values_result = comparator.get_matching_values_at(check_positions)

    print(count_result)
    print(values_result)