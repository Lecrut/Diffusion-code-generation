import datetime

def determine_weekday(year, month, day):
    try:
        date_instance = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e
    
    weekday_mapping = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    
    return weekday_mapping[date_instance.weekday()]

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    
    computed_day = determine_weekday(target_year, target_month, target_day)
    print(computed_day)