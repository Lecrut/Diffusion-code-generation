import datetime

def get_weekday(date_string):
    try:
        parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return parsed_date.strftime("%A")
    except ValueError as validation_error:
        raise ValueError(f"Cannot parse date: {date_string}") from validation_error

def main():
    target_date = "2023-12-25"
    result = get_weekday(target_date)
    print(result)

if __name__ == '__main__':
    main()