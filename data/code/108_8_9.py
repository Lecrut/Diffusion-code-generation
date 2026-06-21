class DateParser:
    _DATE_STRING = "Friday, December 25, 2020"

    @staticmethod
    def _parse_date(date_string: str):
        from dateutil import parser
        return parser.parse(date_string)

    @staticmethod
    def get_day(date_string: str) -> int:
        parsed_date = DateParser._parse_date(date_string)
        return parsed_date.day

if __name__ == '__main__':
    sample_date = DateParser._DATE_STRING
    day = DateParser.get_day(sample_date)
    print(day)