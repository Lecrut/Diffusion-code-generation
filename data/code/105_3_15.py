from datetime import date
import calendar

def find_next_15th_after_reference():
    reference_date = date(2023, 3, 3)
    target_month = reference_date.month + 1
    target_year = reference_date.year
    if target_month > 12:
        target_month = 1
        target_year += 1
    last_day = calendar.monthrange(target_year, target_month)[1]
    if last_day < 15:
        target_month += 1
        target_year = target_year
        if target_month > 12:
            target_month = 1
            target_year += 1
    return date(target_year, target_month, 15)

if __name__ == '__main__':
    result = find_next_15th_after_reference()
    print(result)