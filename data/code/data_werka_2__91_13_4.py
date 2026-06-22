class BooleanOps:
    NOT_MASK = 0x1
    ZERO = 0x0
    ONE = 0x1

    @staticmethod
    def to_int(val: bool) -> int:
        return int(val)

    @staticmethod
    def from_int(val: int) -> bool:
        return bool(val & 1)

    @staticmethod
    def bitwise_negate(val: bool) -> bool:
        int_val = BooleanOps.to_int(val)
        flipped = int_val ^ BooleanOps.NOT_MASK
        return BooleanOps.from_int(flipped)

def negate_boolean(value: bool) -> bool:
    return BooleanOps.bitwise_negate(value)

if __name__ == '__main__':
    val1 = True
    val2 = False
    res1 = negate_boolean(val1)
    res2 = negate_boolean(val2)
    print(res1)
    print(res2)