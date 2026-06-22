class DateParser:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def validate_format(date_str: str) -> bool:
        if not isinstance(date_str, str):
            return False
        try:
            parts = date_str.split("-")
            if len(parts) != 3:
                return False
            if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
                return False
            int(parts[0])
            int(parts[1])
            int(parts[2])
            return True
        except ValueError:
            return False

    @classmethod
    def extract_day(cls, date_str: str) -> str:
        if not cls.validate_format(date_str):
            raise ValueError(f"Invalid date format: {date_str}")
        return date_str.split("-")[2]

if __name__ == '__main__':
    sample_date = "2024-01-15"
    day_value = DateParser.extract_day(sample_date)
    print(day_value)