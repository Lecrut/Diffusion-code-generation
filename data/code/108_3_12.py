class DateParser:
    def get_day_of_month(self, date_str):
        match = re.match(r'^\d{4}-\d{2}-(\d{2})$', date_str)
        if match:
            return int(match.group(1))
        else:
            raise ValueError("Invalid date format")

if __name__ == '__main__':
    parser = DateParser()
    sample_date1 = "2023-04-15"
    day1 = parser.get_day_of_month(sample_date1)
    print(f"Date: {sample_date1}, Day of the month: {day1}")
    sample_date2 = "2023-12-25"
    day2 = parser.get_day_of_month(sample_date2)
    print(f"Date: {sample_date2}, Day of the month: {day2}")