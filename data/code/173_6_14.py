class GroupingGenerator:
    def __init__(self, data, key_func):
        self.data = iter(data)
        self.key_func = key_func
        self.current_group = None
        self.next_item = next(self.data, None)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current_group is not None and len(self.current_group) > 0:
                return self.current_group
            if self.next_item is None:
                raise StopIteration
            key = self.key_func(self.next_item)
            if self.current_group is None or key != self.current_group_key:
                if self.current_group is not None:
                    yield self.current_group
                self.current_group = []
                self.current_group_key = key
            self.current_group.append(self.next_item)
            self.next_item = next(self.data, None)

if __name__ == '__main__':
    sample_data = [
        "apple,red,fruit",
        "banana,yellow,fruit",
        "carrot,orange,vegetable",
        "grape,purple,fruit",
        "spinach,green,vegetable"
    ]

    def key_func(item):
        return item.split(',')[2].strip()

    grouping_gen = GroupingGenerator(sample_data, key_func)
    for group in grouping_gen:
        print(group)