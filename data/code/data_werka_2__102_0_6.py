import datetime

class DateValidator:
    EXPECTED_LENGTH = 10
    SEPARATOR_POS_1 = 4
    SEPARATOR_POS_2 = 7
    SEPARATOR_CHAR = '-'
    MAX_WEEKDAY_INDEX = 4

    @staticmethod
    def _validate_format(date_string):
        if not isinstance(date_string, str):
            raise ValueError("Input must be a string")
        if len(date_string) != DateValidator.EXPECTED_LENGTH:
            raise ValueError("Invalid date format: length mismatch")
        if date_string[DateValidator.SEPARATOR_POS_1] != DateValidator.SEPARATOR_CHAR:
            raise ValueError("Invalid date format: missing first separator")
        if date_string[DateValidator.SEPARATOR_POS_2] != DateValidator.SEPARATOR_CHAR:
            raise ValueError("Invalid date format: missing second separator")
        try:
            int(date_string[0:4])
            int(date_string[5:7])
            int(date_string[8:10])
        except ValueError:
            raise ValueError("Invalid date format: non-numeric components")

    @classmethod
    def is_weekday(cls, date_string: str) -> bool:
        cls._validate_format(date_string)
        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
        try:
            date_obj = datetime.date(year, month, day)
            return date_obj.weekday() <= cls.MAX_WEEKDAY_INDEX
        except ValueError:
            raise ValueError(f"Invalid date value: {date_string}")

if __name__ == '__main__':
    test_cases = [
        "2023-10-07",
        "2023-10-08",
        "2023-02-28",
        "2024-02-29",
        "2023-02-29",
        "not-a-date",
        "2023-13-01",
        "2023-10-7",
        12345
    ]
    for date_str in test_cases:
        try:
            result = DateValidator.is_weekday(date_str)
            print(f"{date_str}: {result}")
        except ValueError as e:
            print(f"{date_str}: Error - {e}")