class DateCalculator:
    def get_day_of_month(self, date_string: str) -> int:
        from datetime import datetime
        try:
            date_object = datetime.strptime(date_string, "%Y-%m-%d")
            return date_object.day
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    calculator = DateCalculator()
    date_str1 = "2023-10-27"
    date_str2 = "1999-01-01"
    date_str3 = "2024-02-29"
    print(f"Day of the month for {date_str1}: {calculator.get_day_of_month(date_str1)}")
    print(f"Day of the month for {date_str2}: {calculator.get_day_of_month(date_str2)}")
    print(f"Day of the month for {date_str3}: {calculator.get_day_of_month(date_str3)}")