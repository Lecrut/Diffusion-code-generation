def group_records(records, key_field):
    groups = {}
    for record in records:
        key_value = record[key_field]
        if key_value not in groups:
            groups[key_value] = []
        groups[key_value].append(record)
    return groups

class Record:
    def __init__(self, id, category, value):
        self.id = id
        self.category = category
        self.value = value

def record_generator():
    for i in range(1, 6):
        yield {'id': i, 'category': chr(ord('A') + (i - 1) % 3), 'value': i * 10}

if __name__ == '__main__':
    sample_records = list(record_generator())
    grouped_records = group_records(sample_records, 'category')
    print(grouped_records)