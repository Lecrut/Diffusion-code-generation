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

class RecordGroupGenerator:
    def __init__(self, records, key_field):
        self.records = iter(records)
        self.key_field = key_field
        self.current_group = None
        self.next_key = None
        self.next_records = []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current_group:
            self._load_next_group()
        if not self.current_group:
            raise StopIteration
        result = next(self.current_group)
        self._prepare_next_group()
        return result

    def _load_next_group(self):
        while self.next_key is None:
            record = next(self.records, None)
            if record is None:
                break
            key_value = getattr(record, self.key_field)
            if self.next_key is None or key_value != self.next_key:
                if self.next_records:
                    self.current_group = iter(self.next_records)
                    self.next_records = []
                self.next_key = key_value

    def _prepare_next_group(self):
        record = next(self.records, None)
        while record and getattr(record, self.key_field) == self.next_key:
            self.next_records.append(record)
            record = next(self.records, None)

if __name__ == '__main__':
    records = [
        Record(1, 'A', 10),
        Record(2, 'B', 20),
        Record(3, 'A', 30),
        Record(4, 'C', 40),
        Record(5, 'B', 50)
    ]
    generator = RecordGroupGenerator(records, 'category')
    for category_group in generator:
        print(category_group.key_field, [record.value for record in category_group])