def format_date(date_str):
    month_dict = {
        '01': 'January', '02': 'February', '03': 'March',
        '04': 'April', '05': 'May', '06': 'June',
        '07': 'July', '08': 'August', '09': 'September',
        '10': 'October', '11': 'November', '12': 'December'
    }
    day, month, year = date_str.split('-')
    return f"{day} {month_dict[month]} {year}"

if __name__ == '__main__':
    sample_date = "2022-11-11"
    print(format_date(sample_date))