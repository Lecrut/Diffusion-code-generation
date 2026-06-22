import re

class DateParser:
    DAY_PATTERN = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')
    DAY_INDEX = 2

    @staticmethod
    def extract_day(date_str: str) -> int:
        match = DateParser.DAY_PATTERN.match(date_str)
        if not match:
            raise ValueError(f"Invalid date format: {date_str}")
        return int(match.group(DateParser.DAY_INDEX))

if __name__ == '__main__':
    sample_date = "1999-01-01"
    day_value = DateParser.extract_day(sample_date)
    print(day_value)