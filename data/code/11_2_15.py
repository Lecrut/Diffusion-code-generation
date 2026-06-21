class TailExtractor:
    _SINGLE_ITEM_SLICE = slice(-1, None)

    @staticmethod
    def _extract_item(sequence):
        return sequence[TailExtractor._SINGLE_ITEM_SLICE][0]

    @classmethod
    def get_last_element(cls, data):
        return cls._extract_item(data)

if __name__ == '__main__':
    values = [100, 200, 300, 400, 500]
    result = TailExtractor.get_last_element(values)
    print(result)