class ListCombiner:
    def __init__(self, initial_list):
        self.list = initial_list.copy()

    def extend_with(self, other_list):
        self.list.extend(other_list)

    def get_result(self):
        return self.list

if __name__ == '__main__':
    combiner = ListCombiner([1, 2, 3])
    combiner.extend_with([4, 5, 6])
    result = combiner.get_result()
    print(result)