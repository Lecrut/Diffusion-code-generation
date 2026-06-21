class Record:
    def __init__(self, id, category, value):
        self.id = id
        self.category = category
        self.value = value

def group_by_field(records, field):
    groups = {}
    for record in records:
        key = getattr(record, field)
        if key not in groups:
            groups[key] = []
        yield key, record

if __name__ == '__main__':
    records = [
        Record(1, 'A', 10),
        Record(2, 'B', 20),
        Record(3, 'A', 30),
        Record(4, 'C', 40),
        Record(5, 'B', 50)
    ]
    
    grouped_generator = group_by_field(records, 'category')
    for category, record in grouped_generator:
        print(f"Category: {category}, Record ID: {record.id}, Value: {record.value}")