class DataGrouper:
    def group_by_attribute(self, records, attribute):
        groups = {}
        for record in records:
            key = getattr(record, attribute)
            if key is None:
                key = "__none__"
            if key not in groups:
                groups[key] = []
            groups[key].append(record)
        return groups
if __name__ == '__main__':
    class Record:
        def __init__(self, id, category, value):
            self.id = id
            self.category = category
            self.value = value
    data = [
        Record(1, 'A', 10),
        Record(2, 'B', 20),
        Record(3, 'A', 30),
        Record(4, 'C', 40),
        Record(5, 'B', 50)
    ]
    grouper = DataGrouper()
    grouped_data = grouper.group_by_attribute(data, 'category')
    print(grouped_data)