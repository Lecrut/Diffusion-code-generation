class SequenceHandler:
    DEFAULT_VALUE = None

    @staticmethod
    def get_first_element(sequence):
        if not sequence:
            return SequenceHandler.DEFAULT_VALUE
        return sequence[0]

if __name__ == '__main__':
    sample_data = {
        'list': [1, 2, 3],
        'tuple': (4, 5, 6),
        'empty_list': [],
        'empty_tuple': (),
        'string': "hello",
        'none': None,
        'number': 123
    }
    
    for key, value in sample_data.items():
        print(f"First element of {key}: {SequenceHandler.get_first_element(value)}")