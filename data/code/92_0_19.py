class BooleanInverter:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def invert(val):
        return not val

def invert_boolean(b):
    return BooleanInverter.invert(b)

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))