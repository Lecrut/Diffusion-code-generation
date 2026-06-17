from datetime import date, timedelta
def add_months(current_date: date, months_to_add: list[int]) -> list[date]:
    result = []
    for m in months_to_add:
        new_month = current_date.month + m
        while True:
            try:
                next_day = date(current_date.year, new_month, current_date.day)
                break
            except ValueError:
                new_month -= 1
                if new_month < 1:
                    new_month = 12
                    current_date.year += -1
        result.append(next_day)
    return result
if __name__ == '__main__':
    sample_dates = [date(2023, 5, 1), date(2024, 7, 1)]
    increments = [1, 6]
    output_list = add_months(sample_dates[0], increments) + add_months(sample_dates[1], increments)
    print(output_list)