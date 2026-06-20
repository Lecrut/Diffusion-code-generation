class FilterValidator:
    def __init__(self):
        self.valid_entries = []

    def add_entry(self, entry):
        if entry is not None and entry != '':
            self.valid_entries.append(entry)

    def get_valid_entries(self):
        return self.valid_entries

if __name__ == '__main__':
    validator = FilterValidator()
    validator.add_entry('hello')
    validator.add_entry('')
    validator.add_entry(None)
    validator.add_entry('world')
    validator.add_entry(' ')
    validator.add_entry('test')
    print(validator.get_valid_entries())