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

def records_generator():
    yield Record(1, 'Apple', 'Fruit')
    yield Record(2, 'Banana', 'Fruit')
    yield Record(3, 'Carrot', 'Vegetable')
    yield Record(4, 'Avocado', 'Fruit')

if __name__ == '__main__':
    records = records_generator()
    grouped_records = group_by_field(records, 'category')
    print(grouped_records)