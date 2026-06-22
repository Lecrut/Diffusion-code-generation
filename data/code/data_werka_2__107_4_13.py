class DateTransformer:
    INPUT_FORMAT = "%d.%m.%Y"
    OUTPUT_FORMAT = "%Y-%m-%d"

    @staticmethod
    def _parse(date_string: str):
        from datetime import datetime
        return datetime.strptime(date_string, DateTransformer.INPUT_FORMAT)

    @staticmethod
    def _format(dt_obj):
        return dt_obj.strftime(DateTransformer.OUTPUT_FORMAT)

    def transform(self, date_string: str) -> str:
        parsed_dt = self._parse(date_string)
        return self._format(parsed_dt)

if __name__ == '__main__':
    transformer = DateTransformer()
    print(transformer.transform("15.08.2021"))
    print(transformer.transform("31.12.1999"))
    print(transformer.transform("01.01.2000"))
    print(transformer.transform("29.02.2024"))