class DataGrouper:
    def group_by(self, records, key_attribute):
        groups = {}
        for record in records:
            key = record[key_attribute]
            if key not in groups:
                groups[key] = []
            groups[key].append(record)
        return groups
if __name__ == '__main__':
    data = [
        {'id': 1, 'category': 'A', 'value': 10},
        {'id': 2, 'category': 'B', 'value': 20},
        {'id': 3, 'category': 'A', 'value': 30},
        {'id': 4, 'category': 'C', 'value': 40},
        {'id': 5, 'category': 'B', 'value': 50}
    ]
    grouper = DataGrouper()
    grouped_data = grouper.group_by(data, 'category')
    print(grouped_data)