from datetime import date, timedelta

def calculate_first_sunday_after_jan_1_2024():
    reference_date = date(2024, 1, 1)
    if reference_date.weekday() == 6:
        return reference_date + timedelta(days=7)
    days_until_sunday = 6 - reference_date.weekday()
    return reference_date + timedelta(days=days_until_sunday)

if __name__ == '__main__':
    result = calculate_first_sunday_after_jan_1_2024()
    print(result)