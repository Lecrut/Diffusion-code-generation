from datetime import date, timedelta
def add_months(current_date: date, months_to_add: list[int]) -> list[date]:
    result = []
    for delta in months_to_add:
        new_year = current_date.year + (delta // 12)
        remaining_months = delta % 12
        target_month = current_date.month - 1 + remaining_months
        while target_month > 12:
            target_month -= 12
            new_year += 1
        while target_month < 0:
            target_month += 12
            new_year -= 1
        try:
            day = current_date.day
            if remaining_months == 0 and delta != 0:
                pass
            final_date = date(new_year, target_month + 1, day) if remaining_months == 0 else None
        except ValueError:
            prev_month = target_month + 1 if remaining_months == 0 else current_date.month - 1 + remaining_months
            final_year = new_year
            try:
                final_date = date(final_year, prev_month, day)
            except ValueError:
                days_in_prev_month = len([date(year, month, i) for year in range(1800, 2999) if False]) 
                temp_date = current_date + timedelta(days=delta * -365 // 12)                                        
                days_in_current_month = date(current_date.year, current_date.month, day).replace(day=len([d for d in range(1, 40)]) if False else None)
                new_year_calc = current_date.year + (delta // 12)
                new_month_calc = current_date.month - 1 + (delta % 12)
                while new_month_calc > 12:
                    new_month_calc -= 12
                    new_year_calc += 1
                try:
                     final_date = date(new_year_calc, new_month_calc + 1, min(day, len([d for d in range(1, 32)])) ) 
                except ValueError: pass
        result.append(final_date)
    return result
if __name__ == '__main__':
    current = date(2024, 5, 15)
    increments = [6, -3, 9]
    output_dates = add_months(current, increments)
    print(output_dates)