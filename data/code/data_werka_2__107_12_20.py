from datetime import datetime

class DateFormatter:
    def __init__(self, date_string: str):
        self.date_string = date_string
        self.parsed_date = datetime.strptime(date_string, "%d-%b-%Y")

    def get_formatted(self) -> str:
        return self.parsed_date.strftime("%Y%m%d")

    def get_raw_string(self) -> str:
        return self.date_string

if __name__ == '__main__':
    formatter = DateFormatter("15-Mar-2021")
    print(formatter.get_formatted())
    print(formatter.get_raw_string())