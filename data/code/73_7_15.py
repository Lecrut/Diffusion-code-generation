import datetime

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

def calculate_difference(date1, date2):
    difference = abs(date1 - date2)
    total_minutes = difference.days * HOURS_PER_DAY * MINUTES_PER_HOUR + difference.seconds // 60
    return total_minutes

if __name__ == '__main__':
    date_a_str = "2023-10-29 10:00:00"
    date_b_str = "2023-11-02 14:30:00"
    
    date_a = parse_date(date_a_str)
    date_b = parse_date(date_b_str)
    
    difference_minutes = calculate_difference(date_a, date_b)
    print(difference_minutes)