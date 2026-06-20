from datetime import datetime

class DateDifference:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def date_difference(date_str1: str, date_str2: str) -> (int, int, int):
        date1 = datetime.strptime(date_str1, DateDifference.DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DateDifference.DATE_FORMAT)
        diff = abs(date2 - date1)
        total_seconds = int(diff.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds

if __name__ == '__main__':
    result1 = DateDifference.date_difference("2023-10-01", "2023-10-05")
    print(f"Hours: {result1[0]}, Minutes: {result1[1]}, Seconds: {result1[2]}")

    result2 = DateDifference.date_difference("2024-05-15", "2024-04-15")
    print(f"Hours: {result2[0]}, Minutes: {result2[1]}, Seconds: {result2[2]}")