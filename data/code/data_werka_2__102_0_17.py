import datetime

class DateValidator:
    EXPECTED_LENGTH = 10
    SEPARATOR_MONTH = 4
    SEPARATOR_DAY = 7
    VALID_WEEKDAY_MAX = 4

    @staticmethod
    def _validate_format(date_string: str) -> bool:
        if not isinstance(date_string, str):
            raise ValueError("Input must be a string")
        if len(date_string) != DateValidator.EXPECTED_LENGTH:
            raise ValueError("Invalid date format: length mismatch")
        if date_string[DateValidator.SEPARATOR_MONTH] != '-' or date_string[DateValidator.SEPARATOR_DAY] != '-':
            raise ValueError("Invalid date format: missing separators")
        return True

    @staticmethod
    def _parse_date(date_string: str) -> datetime.date:
        try:
            year = int(date_string[0:4])
            month = int(date_string[5:7])
            day = int(date_string[8:10])
            return datetime.date(year, month, day)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_string}")

    @staticmethod
    def is_weekday(date_string: str) -> bool:
        DateValidator._validate_format(date_string)
        parsed_date = DateValidator._parse_date(date_string)
        return parsed_date.weekday() <= DateValidator.VALID_WEEKDAY_MAX

if __name__ == '__main__':
    test_dates = ["2023-10-07", "2023-10-08", "invalid", "2023-02-29"]
    for d in test_dates:
        try:
            print(DateValidator.is_weekday(d))
        except ValueError as e:
            print(e)