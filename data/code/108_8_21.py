from dateutil.parser import parse

class DateExtractor:
    def __init__(self, raw_input: str):
        self._parsed = parse(raw_input)

    def get_day(self) -> int:
        return self._parsed.day

if __name__ == '__main__':
    extractor = DateExtractor("December 25, 2024")
    print(extractor.get_day())