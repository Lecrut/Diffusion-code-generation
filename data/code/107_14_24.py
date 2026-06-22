from datetime import datetime

class DateConverter:
    INPUT_FMT = "%d-%m-%Y %H:%M:%S"
    OUTPUT_FMT = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def _parse(raw: str) -> datetime:
        return datetime.strptime(raw, DateConverter.INPUT_FMT)

    @staticmethod
    def _format(dt: datetime) -> str:
        return dt.strftime(DateConverter.OUTPUT_FMT)

    @classmethod
    def convert(cls, raw: str) -> str:
        parsed = cls._parse(raw)
        return cls._format(parsed)

if __name__ == '__main__':
    sample = '15-08-2024 09:15:30'
    result = DateConverter.convert(sample)
    print(result)