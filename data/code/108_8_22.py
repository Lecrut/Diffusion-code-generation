from dateutil.parser import parse

class DateProcessor:
    def __init__(self, input_date: str):
        self.date_obj = parse(input_date)

    def get_day(self) -> int:
        return self.date_obj.day

    def get_month_name(self) -> str:
        return self.date_obj.strftime("%B")

if __name__ == '__main__':
    processor = DateProcessor("2024-02-29")
    print(processor.get_day())
    print(processor.get_month_name())