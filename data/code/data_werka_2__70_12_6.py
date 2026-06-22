class BoundaryExtractor:
    FIRST_INDEX = 0
    LAST_INDEX = -1

    @staticmethod
    def _validate_sequence(seq):
        if not seq:
            raise ValueError("Sequence must contain at least one element")
        return seq

    @classmethod
    def extract(cls, seq):
        validated = cls._validate_sequence(seq)
        first_val = validated[cls.FIRST_INDEX]
        last_val = validated[cls.LAST_INDEX]
        return first_val, last_val

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = BoundaryExtractor.extract(data)
    print(result)