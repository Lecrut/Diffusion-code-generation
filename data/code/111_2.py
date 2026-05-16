def extract_date_parts(date_string):
    try:
        year, month, day = map(int, date_string.split('-'))
        return year, month, day
    except ValueError:
        raise ValueError("Invalid date format. Expected 'YYYY-MM-DD'.")
if __name__ == '__main__':
    date1 = "2023-10-27"
    date2 = "1999-01-01"
    date3 = "2024/05/15"
    date4 = "2023-13-01"
    print(f"Processing {date1}:")
    try:
        year, month, day = extract_date_parts(date1)
        print(f"Year: {year}, Month: {month}, Day: {day}")
    except ValueError as e:
        print(f"Error: {e}")
    print(f"\nProcessing {date2}:")
    try:
        year, month, day = extract_date_parts(date2)
        print(f"Year: {year}, Month: {month}, Day: {day}")
    except ValueError as e:
        print(f"Error: {e}")
    print(f"\nProcessing {date3}:")
    try:
        year, month, day = extract_date_parts(date3)
        print(f"Year: {year}, Month: {month}, Day: {day}")
    except ValueError as e:
        print(f"Error: {e}")
    print(f"\nProcessing {date4}:")
    try:
        year, month, day = extract_date_parts(date4)
        print(f"Year: {year}, Month: {month}, Day: {day}")
    except ValueError as e:
        print(f"Error: {e}")