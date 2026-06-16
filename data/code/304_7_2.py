import datetime
def compare_dates(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
        if date1 < date2:
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2023-02-20"
    try:
        result = compare_dates(date1_input, date2_input)
        if result:
            print(f"{date1_input} is before {date2_input}")
        else:
            print(f"{date1_input} is not before {date2_input}")
    except ValueError as ve:
        print(f"Error during date processing: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")