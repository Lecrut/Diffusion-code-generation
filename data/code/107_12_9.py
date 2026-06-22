class DateConverter:
    MONTHS = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    @classmethod
    def convert(cls, date_str: str) -> str:
        if not isinstance(date_str, str):
            raise TypeError("Input must be a string")
        parts = date_str.split("-")
        if len(parts) != 3:
            raise ValueError("Invalid date format")
        day_str, month_str, year_str = parts
        if month_str not in cls.MONTHS:
            raise ValueError(f"Invalid month: {month_str}")
        day = int(day_str)
        year = int(year_str)
        month = cls.MONTHS[month_str]
        return f"{year:04d}{month:02d}{day:02d}"

if __name__ == '__main__':
    date_input = "15-Mar-2024"
    output = DateConverter.convert(date_input)
    print(output)