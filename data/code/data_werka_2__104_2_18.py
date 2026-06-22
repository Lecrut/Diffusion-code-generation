class TimestampComparator:
    SECOND = 1

    @staticmethod
    def validate_int(value):
        if not isinstance(value, int):
            raise ValueError("Argument must be an integer")
        return value

    @classmethod
    def compute_diff(cls, ts1, ts2):
        cls.validate_int(ts1)
        cls.validate_int(ts2)
        return abs(ts1 - ts2)

if __name__ == '__main__':
    comp = TimestampComparator()
    result = comp.compute_diff(1672531200, 1672531260)
    print(result)