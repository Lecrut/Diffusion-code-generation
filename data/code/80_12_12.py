import datetime

class DateOrderer:
    def order_dates(self, date1: datetime.date, date2: datetime.date) -> tuple:
        return (date1, date2) if date1 < date2 else (date2, date1)

if __name__ == '__main__':
    orderer = DateOrderer()
    date_a = datetime.date(2023, 10, 26)
    date_b = datetime.date(2023, 10, 20)
    print(orderer.order_dates(date_a, date_b))