from datetime import datetime
import calendar

def format_date_custom(date_input):
    if isinstance(date_input, datetime):
        current_date = date_input
    elif isinstance(date_input, str):
        current_date = datetime.strptime(date_input, '%Y-%m-%d')
    else:
        raise ValueError("Unsupported input type")
    
    day_of_week_index = current_date.weekday()
    day_name = calendar.day_name[day_of_week_index]
    month_name = calendar.month_name[current_date.month]
    day_value = current_date.day
    year_value = current_date.year
    
    formatted_day = f"{day_value:02d}"
    return f"{day_name}, {month_name} {formatted_day}, {year_value}"

if __name__ == '__main__':
    sample_input = datetime(1999, 12, 31)
    output = format_date_custom(sample_input)
    print(output)