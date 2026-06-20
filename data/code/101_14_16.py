from datetime import date

class DateInfo:
    def __init__(self):
        self.day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def get_day_info(self, dt: date) -> tuple[str, int]:
        day_index = dt.weekday()
        day_name = self.day_names[day_index]
        day_number = day_index + 1
        return (day_name, day_number)

if __name__ == '__main__':
    sample_date = date(2025, 3, 15)
    date_info_instance = DateInfo()
    result = date_info_instance.get_day_info(sample_date)
    print(f"Date: {sample_date}, Day Name: {result[0]}, Day Number: {result[1]}")