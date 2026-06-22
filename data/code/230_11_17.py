class DictionaryProcessor:
    def process_dict(self, input_dict):
        for key, value in input_dict.items():
            print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    processor = DictionaryProcessor()
    sample_dict = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    processor.process_dict(sample_dict)