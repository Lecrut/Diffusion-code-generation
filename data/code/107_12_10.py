from datetime import datetime

class DateFormatter:
    def __init__(self, date_string: str):
        self.date_string = date_string

    def to_ymd(self) -> str:
        dt = datetime.strptime(self.date_string, "%d-%b-%Y")
        return dt.strftime("%Y%m%d")

    def get_original(self) -> str:
        return self.date_string

if __name__ == '__main__':
    formatter = DateFormatter("15-Mar-2022")
    print(formatter.to_ymd())
    print(formatter.get_original())