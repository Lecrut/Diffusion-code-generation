class DictFormatter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    def format_pairs(self):
        return [f"Key: {key}, Value: {value}" for key, value in self.dictionary.items()]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    formatter = DictFormatter(sample_dict)
    formatted_pairs = formatter.format_pairs()
    for pair in formatted_pairs:
        print(pair)