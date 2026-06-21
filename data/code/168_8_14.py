def group_by_length(items):
    groups = {}
    for item in items:
        length = len(str(item))
        if length not in groups:
            groups[length] = []
        groups[length].append(item)
    return groups

class GroupByLength:
    def __init__(self, items):
        self.items = items
        self.groups = group_by_length(items)

    def get_groups(self):
        return self.groups

if __name__ == '__main__':
    sample_items = [12345, 'hello', 789, 'world!', 1, 2, 3]
    gbl = GroupByLength(sample_items)
    print(gbl.get_groups())