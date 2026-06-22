import datetime

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_weekday(self):
        return self.date_obj.strftime('%A').upper()

def analyze_date(year, month, day):
    if year < 1 or year > 9999:
        raise ValueError("Year out of range")
    if month < 1 or month > 12:
        raise ValueError("Month out of range")
    if day < 1 or day > 31:
        raise ValueError("Day out of range")
    try:
        analyzer = DateAnalyzer(year, month, day)
        return analyzer.get_weekday()
    except ValueError:
        raise ValueError("Invalid date provided")

if __name__ == '__main__':
    result = analyze_date(2024, 7, 4)
    print(result)