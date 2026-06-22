class ArrayIndexComparator:
    def __init__(self, array_one, array_two):
        self.array_one = array_one
        self.array_two = array_two

    def count_matches(self, indices):
        count = 0
        for index in indices:
            if index < len(self.array_one) and index < len(self.array_two):
                if self.array_one[index] == self.array_two[index]:
                    count += 1
        return count

    def get_matching_values(self, indices):
        values = []
        for index in indices:
            if index < len(self.array_one) and index < len(self.array_two):
                if self.array_one[index] == self.array_two[index]:
                    values.append(self.array_one[index])
        return values

if __name__ == '__main__':
    data_a = [5, 10, 15, 20, 25]
    data_b = [5, 12, 15, 22, 25]
    check_positions = [0, 2, 3, 4]
    comparator = ArrayIndexComparator(data_a, data_b)
    match_count = comparator.count_matches(check_positions)
    match_values = comparator.get_matching_values(check_positions)
    print(match_count)
    print(match_values)