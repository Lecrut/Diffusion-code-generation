def group_by_field(records, field):
    groups = {}
    for record in records:
        key = getattr(record, field)
        if key not in groups:
            groups[key] = []
        groups[key].append(record)
    return groups

class Record:
    def __init__(self, id, category, value):
        self.id = id
        self.category = category
        self.value = value

def main():
    records = [
        Record(1, 'A', 10),
        Record(2, 'B', 20),
        Record(3, 'A', 30),
        Record(4, 'C', 40),
        Record(5, 'B', 50)
    ]
    
    grouped_records = group_by_field(records, 'category')
    for category, records in grouped_records.items():
        print(f"Category: {category}")
        for record in records:
            print(f"  ID: {record.id}, Value: {record.value}")

if __name__ == '__main__':
    main()