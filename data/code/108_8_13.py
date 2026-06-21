from dateutil.parser import parse

class DateExtractor:
    DAY_FORMAT = "%d"

    @staticmethod
    def get_day(date_string: str) -> int:
        parsed_date = parse(date_string)
        return parsed_date.day

if __name__ == '__main__':
    sample_input = "December 25, 2024"
    extractor = DateExtractor()
    day_value = extractor.get_day(sample_input)
    print(day_value)