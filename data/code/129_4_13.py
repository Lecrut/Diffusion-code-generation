class UniqueList:
    def __init__(self):
        self.seen = set()
        self.result = []

    def add(self, item):
        if item not in self.seen:
            self.seen.add(item)
            self.result.append(item)

    def get_unique_list(self):
        return self.result

if __name__ == '__main__':
    unique_list_instance = UniqueList()
    sample_values = [1, 2, 3, 2, 4, 3, 5]
    for value in sample_values:
        unique_list_instance.add(value)
    print(unique_list_instance.get_unique_list())