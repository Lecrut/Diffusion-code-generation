from datetime import datetime

class DayOfWeekCalculator:
    DAY_NAMES = [
        "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY",
        "FRIDAY", "SATURDAY", "SUNDAY"
    ]

    @staticmethod
    def get_day_of_week(date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        day_index = date_obj.weekday()
        return DayOfWeekCalculator.DAY_NAMES[day_index]

if __name__ == '__main__':
    result = DayOfWeekCalculator.get_day_of_week('2023-11-11')
    print(result)