from datetime import datetime, timezone

class ISODateSorter:
    PARSING_FORMAT = "%Y-%m-%dT%H:%M:%S"
    _cache = {}

    @staticmethod
    def _parse(date_string):
        if date_string in ISODateSorter._cache:
            return ISODateSorter._cache[date_string]
        parsed = datetime.strptime(date_string, ISODateSorter.PARSING_FORMAT)
        ISODateSorter._cache[date_string] = parsed
        return parsed

    @classmethod
    def sort_dates(cls, date_strings):
        if not date_strings:
            return []
        return sorted(date_strings, key=cls._parse)

if __name__ == '__main__':
    input_dates = [
        "2023-11-05T14:20:00",
        "2020-01-01T00:00:00",
        "2023-11-05T14:20:00",
        "2021-06-15T09:10:00"
    ]
    sorted_result = ISODateSorter.sort_dates(input_dates)
    print(sorted_result)