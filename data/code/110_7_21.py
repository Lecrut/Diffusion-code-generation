from datetime import datetime

def sort_date_strings(date_list):
    if not isinstance(date_list, list):
        raise ValueError("Input must be a list")
    
    parsed_dates = []
    for date_str in date_list:
        if not isinstance(date_str, str):
            raise ValueError("All elements must be strings")
        try:
            dt = datetime.strptime(date_str, "%m-%d-%Y")
            parsed_dates.append((dt, date_str))
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
    
    parsed_dates.sort(key=lambda x: x[0])
    
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    dates = ["12-31-2023", "01-01-2023", "06-15-2022", "02-28-2023"]
    sorted_dates = sort_date_strings(dates)
    print(sorted_dates)