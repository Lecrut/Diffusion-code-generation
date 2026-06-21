class UniqueValues:
    def __init__(self):
        self.values = dict.fromkeys([], None)

    def add_value(self, value):
        if value not in self.values:
            self.values[value] = True

    def get_unique_values(self):
        return list(self.values.keys())

if __name__ == '__main__':
    sample_data = [10, 20, 30, 20, 40, 50, 10]
    unique_processor = UniqueValues()
    for value in sample_data:
        unique_processor.add_value(value)
    final_results = unique_processor.get_unique_values()
    print(final_results)