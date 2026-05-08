from datetime import date
def determine_weekday(date_obj):
    return date_obj.strftime("%A")
if __name__ == '__main__':
    sample_date_1 = date(2023, 10, 26)
    print(determine_weekday(sample_date_1))
    sample_date_2 = date(2024, 1, 1)
    print(determine_weekday(sample_date_2))
    sample_date_3 = date(2025, 12, 31)
    print(determine_weekday(sample_date_3))