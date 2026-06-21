class Record:
    def __init__(self, id, category, value):
        self.id = id
        self.category = category
        self.value = value

def group_records(records, key_field):
    groups = {}
    for record in records:
        key_value = getattr(record, key_field)
        if key_value not in groups:
            groups[key_value] = []
        groups[key_value].append(record)
    return groups

if __name__ == '__main__':
    sample_records = [
        Record(1, 'A', 10),
        Record(2, 'B', 20),
        Record(3, 'A', 30),
        Record(4, 'C', 40),
        Record(5, 'B', 50)
    ]
    grouped_records = group_records(sample_records, 'category')
    for category, records in grouped_records.items():
        print(f"Category: {category}")
        for record in records:
            print(f"  ID: {record.id}, Value: {record.value}")