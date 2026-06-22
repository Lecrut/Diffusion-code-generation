from datetime import datetime

class DateConverter:
    def __init__(self, input_format: str, output_format: str):
        self.input_format = input_format
        self.output_format = output_format

    def convert(self, date_string: str) -> str:
        parsed_date = datetime.strptime(date_string, self.input_format)
        return parsed_date.strftime(self.output_format)

if __name__ == '__main__':
    converter = DateConverter("%d.%m.%Y", "%Y-%m-%d")
    print(converter.convert("25.12.2023"))
    print(converter.convert("01.01.2000"))
    print(converter.convert("31.12.1999"))
    print(converter.convert("15.08.2021"))