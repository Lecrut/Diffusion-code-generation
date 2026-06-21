def group_by_field(records, field):
    groups = {}
    for record in records:
        key = getattr(record, field)
        if key not in groups:
            groups[key] = []
        groups[key].append(record)
    return groups

class Record:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

def main():
    records = [
        Record(1, 'Apple', 'Fruit'),
        Record(2, 'Banana', 'Fruit'),
        Record(3, 'Carrot', 'Vegetable'),
        Record(4, 'Avocado', 'Fruit')
    ]
    grouped_records = group_by_field(records, 'category')
    for category, records in grouped_records.items():
        print(f"{category}: {records}")

if __name__ == '__main__':
    main()