class LengthComparer:
    CM_PER_METER = 100

    @staticmethod
    def compare(meters1, meters2):
        cm1 = meters1 * LengthComparer.CM_PER_METER
        cm2 = meters2 * LengthComparer.CM_PER_METER
        if cm1 > cm2:
            return meters1
        else:
            return meters2

if __name__ == '__main__':
    value1 = 6.0
    value2 = 4.5
    comparer = LengthComparer()
    larger_value = comparer.compare(value1, value2)
    print(larger_value)