from datetime import datetime
def compare_dates(date1_str, date2_str):
    try:
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        if date1 < date2:
            return True
        else:
            return False
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2023-02-20"
    result = compare_dates(date1_input, date2_input)
    if isinstance(result, bool):
        print(f"Is {date1_input} before {date2_input}? {result}")
    else:
        print(result)