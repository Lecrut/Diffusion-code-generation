class DateConverter:
    MONTHS = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    @staticmethod
    def convert(date_string: str) -> str:
        parts = date_string.split("-")
        day = int(parts[0])
        month = DateConverter.MONTHS[parts[1]]
        year = int(parts[2])
        return f"{year:04d}{month:02d}{day:02d}"

if __name__ == '__main__':
    sample_date = "15-Mar-2024"
    result = DateConverter.convert(sample_date)
    print(result)