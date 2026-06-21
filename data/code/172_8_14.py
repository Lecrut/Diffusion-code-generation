class FilterMapper:

    def __init__(self):
        self.valid_mapping = {}

    def filter_and_map(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(key, int) and isinstance(value, str):
                self.valid_mapping[key] = value

    def get_valid_value(self, key):
        return self.valid_mapping.get(key)
if __name__ == '__main__':
    sample_dictionary = {1: 'one', 2: 'two', 3: 'three', 4.5: 'four point five', 'five': 'word'}
    mapper = FilterMapper()
    mapper.filter_and_map(sample_dictionary)
    print(mapper.get_valid_value(1))
    print(mapper.get_valid_value(2))
    print(mapper.get_valid_value(3))
    print(mapper.get_valid_value(4.5))
    print(mapper.get_valid_value('five'))