class ListComparator:
    PREFIX = "Greater pair detected:"

    @staticmethod
    def _validate_inputs(list_a, list_b):
        if not isinstance(list_a, list) or not isinstance(list_b, list):
            raise ValueError("Both inputs must be lists")
        return min(len(list_a), len(list_b))

    def compare_and_collect(self, list_a, list_b):
        limit = self._validate_inputs(list_a, list_b)
        matches = []
        for idx in range(limit):
            val_left = list_a[idx]
            val_right = list_b[idx]
            if val_left > val_right:
                matches.append((val_left, val_right))
                print(f"{self.PREFIX} {val_left} > {val_right}")
        return matches

if __name__ == '__main__':
    data_x = [15, 4, 12, 8]
    data_y = [10, 9, 11, 2]
    comparator = ListComparator()
    found_pairs = comparator.compare_and_collect(data_x, data_y)
    print(found_pairs)