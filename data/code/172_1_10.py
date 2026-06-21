class LookupTableBuilder:
    @staticmethod
    def build_lookup_table(keys, values):
        return dict(zip(keys, values))

if __name__ == '__main__':
    sample_keys = ['apple', 'carrot', 'banana', 'broccoli']
    sample_values = ['fruit', 'vegetable', 'fruit', 'vegetable']
    lookup_table = LookupTableBuilder.build_lookup_table(sample_keys, sample_values)
    print(lookup_table)