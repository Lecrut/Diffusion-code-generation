from datetime import datetime

class DateComparator:
    EARLIEST_POSSIBLE = datetime.min
    LATEST_POSSIBLE = datetime.max

    @staticmethod
    def _validate_date(date_obj):
        if not isinstance(date_obj, datetime):
            raise ValueError("Input must be a datetime object")
        return date_obj

    @staticmethod
    def is_earlier(first_date, second_date):
        validated_first = DateComparator._validate_date(first_date)
        validated_second = DateComparator._validate_date(second_date)
        return validated_first < validated_second

if __name__ == '__main__':
    sample_first = datetime(2020, 6, 15, 10, 0, 0)
    sample_second = datetime(2020, 6, 16, 10, 0, 0)
    outcome = DateComparator.is_earlier(sample_first, sample_second)
    print(outcome)