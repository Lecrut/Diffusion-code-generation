class BooleanInverter:
    TRUE_VAL = True
    FALSE_VAL = False

    @staticmethod
    def invert(value):
        return BooleanInverter.FALSE_VAL if value else BooleanInverter.TRUE_VAL

def get_opposite_bools(bool_list):
    return [BooleanInverter.invert(b) for b in bool_list]

if __name__ == '__main__':
    sample_bools = [True, True, False, True, False]
    result = get_opposite_bools(sample_bools)
    print(result)