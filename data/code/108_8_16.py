from dateutil.parser import parse

class DateExtractor:
    def __init__(self, date_string: str):
        self.date_string = date_string

    def get_day(self) -> int:
        try:
            parsed_date = parse(self.date_string)
        except ValueError as e:
            raise ValueError(f"Invalid date format: {self.date_string}") from e
        return parsed_date.day

if __name__ == '__main__':
    extractor = DateExtractor("December 25, 2023")
    day = extractor.get_day()
    print(day)