class TimestampComparator:
    _ZERO = 0.0
    _ONE_YEAR = 31536000.0

    @staticmethod
    def is_first_before_second(ts1: float, ts2: float) -> bool:
        return ts1 < ts2

if __name__ == '__main__':
    comp = TimestampComparator()
    start_time = TimestampComparator._ZERO
    end_time = TimestampComparator._ONE_YEAR
    result = comp.is_first_before_second(start_time, end_time)
    print(result)