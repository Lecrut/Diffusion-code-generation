from datetime import date

def is_valid_date_format(date_str):
    try:
        date_obj = date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

def format_date(date_str):
    if not is_valid_date_format(date_str):
        raise ValueError("Invalid date format")
    
    date_obj = date.fromisoformat(date_str)
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    return f"{date_obj.day} {month_names[date_obj.month - 1]} {date_obj.year}"

if __name__ == '__main__':
    sample_date = "2022-11-11"
    formatted_date = format_date(sample_date)
    print(formatted_date)