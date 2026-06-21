from datetime import datetime

class DateFormatter:
    def __init__(self, input_format: str, output_format: str):
        self.input_format = input_format
        self.output_format = output_format

    def format(self, date_string: str) -> str:
        parsed_date = datetime.strptime(date_string, self.input_format)
        return parsed_date.strftime(self.output_format)

if __name__ == '__main__':
    formatter = DateFormatter("%Y-%m-%d", "%d/%m/%Y")
    sample_date = "2023-10-25"
    result = formatter.format(sample_date)
    print(result)
    leap_date = "2024-02-29"
    leap_result = formatter.format(leap_date)
    print(leap_result)