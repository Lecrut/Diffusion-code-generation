class FilteredMapper:
    def __init__(self):
        self.filtered_map = {}

    def filter_and_map(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(key, int) and isinstance(value, str):
                self.filtered_map[key] = value

    def get_filtered_word(self, key):
        return self.filtered_map.get(key)

if __name__ == '__main__':
    mapper = FilteredMapper()
    sample_dictionary = {
        1: "apple",
        2: "banana",
        3: "carrot",
        4: "broccoli",
        5: "grape"
    }
    mapper.filter_and_map(sample_dictionary)
    print(mapper.get_filtered_word(2))
    print(mapper.get_filtered_word(6))