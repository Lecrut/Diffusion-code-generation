def group_by_field(records, field):
    groups = {}
    for record in records:
        key = getattr(record, field)
        if key not in groups:
            groups[key] = []
        groups[key].append(record)
    return groups

class Record:
    def __init__(self, id, category):
        self.id = id
        self.category = category

def main():
    records = [
        Record(1, 'A'),
        Record(2, 'B'),
        Record(3, 'A'),
        Record(4, 'C'),
        Record(5, 'B')
    ]
    grouped_records = group_by_field(records, 'category')
    for category, records in grouped_records.items():
        print(f"Category: {category}")
        for record in records:
            print(f"  ID: {record.id}")

if __name__ == '__main__':
    main()