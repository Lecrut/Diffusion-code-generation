class ThirdElementAccessor:
    THIRD_INDEX = 2

    @staticmethod
    def _validate_length(sequence, required_length):
        if len(sequence) < required_length:
            raise IndexError(f"Sequence length {len(sequence)} is less than required {required_length}")

    @classmethod
    def get_third(cls, sequence):
        cls._validate_length(sequence, cls.THIRD_INDEX + 1)
        return sequence[cls.THIRD_INDEX]

if __name__ == '__main__':
    data = [100, 200, 300, 400]
    result = ThirdElementAccessor.get_third(data)
    print(result)