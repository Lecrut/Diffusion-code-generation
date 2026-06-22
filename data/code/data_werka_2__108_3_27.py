class DateParser:
    DATE_PATTERN = r"(\d{4})-(\d{2})-(\d{2})"

    @staticmethod
    def _validate_format(date_str):
        if not isinstance(date_str, str):
            raise ValueError("Input must be a string")
        parts = date_str.split("-")
        if len(parts) != 3:
            raise ValueError("Date string must have three parts")
        return parts

    @classmethod
    def extract_day(cls, date_str):
        parts = cls._validate_format(date_str)
        return parts[2]

if __name__ == '__main__':
    sample_date = "2024-01-15"
    day_value = DateParser.extract_day(sample_date)
    print(day_value)