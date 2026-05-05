import datetime
def calculate_time_difference(date_string1, date_string2):
    try:
        date1 = datetime.datetime.strptime(date_string1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_string2, '%Y-%m-%d')
        difference = abs(date1 - date2)
        return difference.days
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2022-11-20"
    date_c = "2023/01/10"
    date_d = "2023-12-31"
    date_e = "2023-01-01"
    print(f"Difference between {date_a} and {date_b}: {calculate_time_difference(date_a, date_b)} days")
    print(f"Difference between {date_a} and {date_c}: {calculate_time_difference(date_a, date_c)}")
    print(f"Difference between {date_d} and {date_e}: {calculate_time_difference(date_d, date_e)} days")
    print(f"Difference between {date_e} and {date_a}: {calculate_time_difference(date_e, date_a)} days")
    print(f"Difference between {date_c} and {date_d}: {calculate_time_difference(date_c, date_d)}")