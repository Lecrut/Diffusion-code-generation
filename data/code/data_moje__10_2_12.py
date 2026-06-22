class TupleProcessor:
    SAMPLE_VALUES = (10, 20, 30, 40, 50)

    @staticmethod
    def get_first(value_tuple):
        return value_tuple[0]

if __name__ == '__main__':
    processor = TupleProcessor()
    result = processor.get_first(processor.SAMPLE_VALUES)
    print(result)