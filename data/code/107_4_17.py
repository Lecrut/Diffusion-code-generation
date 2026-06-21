class DateTransformer:
    INPUT_FORMAT = "%d.%m.%Y"
    OUTPUT_FORMAT = "%Y-%m-%d"

    @staticmethod
    def _parse(date_str: str) -> object:
        from datetime import datetime
        return datetime.strptime(date_str, DateTransformer.INPUT_FORMAT)

    @staticmethod
    def format(date_str: str) -> str:
        dt = DateTransformer._parse(date_str)
        return dt.strftime(DateTransformer.OUTPUT_FORMAT)

if __name__ == '__main__':
    transformer = DateTransformer()
    print(transformer.format("12.03.2024"))
    print(transformer.format("01.01.2000"))
    print(transformer.format("31.12.1999"))