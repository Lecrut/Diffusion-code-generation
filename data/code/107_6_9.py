from datetime import datetime

def format_date(date_str):
    month_map = {
        '01': 'January', '02': 'February', '03': 'March',
        '04': 'April', '05': 'May', '06': 'June',
        '07': 'July', '08': 'August', '09': 'September',
        '10': 'October', '11': 'November', '12': 'December'
    }
    
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_name = date_obj.strftime('%A')
    month_num = date_obj.strftime('%m')
    day_num = date_obj.strftime('%d')
    year = date_obj.strftime('%Y')
    
    formatted_date = f"{day_name}, {month_map[month_num]} {day_num}, {year}"
    return formatted_date

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(format_date(sample_date))