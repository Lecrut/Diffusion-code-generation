class NumericLabelConverter:
    def __init__(self):
        self.key_label_mapping = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five'
        }

    def convert_key_to_label(self, key):
        return self.key_label_mapping.get(key, 'Unknown')

if __name__ == '__main__':
    converter = NumericLabelConverter()
    print(converter.convert_key_to_label(2))
    print(converter.convert_key_to_label(6))