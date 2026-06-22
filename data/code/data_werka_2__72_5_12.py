class ListComparator:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b
        self.limit = min(len(list_a), len(list_b))

    def _determine_relation(self, val_a, val_b):
        if val_a > val_b:
            return 'A > B'
        if val_a < val_b:
            return 'A < B'
        return 'A == B'

    def compare_pairs(self):
        for index in range(self.limit):
            current_a = self.list_a[index]
            current_b = self.list_b[index]
            yield self._determine_relation(current_a, current_b)

if __name__ == '__main__':
    primary_data = [5, 10, 15, 20]
    secondary_data = [5, 8, 15, 22, 30]
    
    comparator_instance = ListComparator(primary_data, secondary_data)
    
    pair_results = list(comparator_instance.compare_pairs())
    print(pair_results)
    
    print(comparator_instance.limit)