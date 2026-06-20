from datetime import date

def calculate_day_of_year(input_date):
    try:
        dt = date.fromisoformat(input_date)
        return dt.timetuple().tm_yday
    except ValueError as e:
        raise ValueError(f"Invalid date format: {input_date}. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    input_date_1 = "2023-04-15"
    result_1 = calculate_day_of_year(input_date_1)
    print(f"Input Date: {input_date_1}, Day of Year: {result_1}")
    
    input_date_2 = "2023-12-25"
    result_2 = calculate_day_of_year(input_date_2)
    print(f"Input Date: {input_date_2}, Day of Year: {result_2}")
    
    input_date_3 = "2022-02-29"
    try:
        result_3 = calculate_day_of_year(input_date_3)
        print(f"Input Date: {input_date_3}, Day of Year: {result_3}")
    except ValueError as e:
        print(e)