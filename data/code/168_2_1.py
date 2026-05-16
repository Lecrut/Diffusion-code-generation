class ItemSorter:
    def group_items(self, items, key):
        groups = {}
        for item in items:
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
        return groups
if __name__ == '__main__':
    sorter = ItemSorter()
    data = [
        {'name': 'Apple', 'category': 'Fruit', 'value': 10},
        {'name': 'Carrot', 'category': 'Vegetable', 'value': 5},
        {'name': 'Banana', 'category': 'Fruit', 'value': 15},
        {'name': 'Broccoli', 'category': 'Vegetable', 'value': 8},
        {'name': 'Orange', 'category': 'Fruit', 'value': 12}
    ]
    category_groups = sorter.group_items(data, 'category')
    print(category_groups)