from datetime import datetime

class DateConverter:
    INPUT_FORMAT = "%d.%m.%Y"
    OUTPUT_FORMAT = "%Y-%m-%d"

    @staticmethod
    def convert(date_str: str) -> str:
        parsed_date = datetime.strptime(date_str, DateConverter.INPUT_FORMAT)
        return parsed_date.strftime(DateConverter.OUTPUT_FORMAT)

if __name__ == '__main__':
    print(DateConverter.convert("15.03.2021"))
    print(DateConverter.convert("01.01.2000"))
    print(DateConverter.convert("31.12.1999"))