from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    day_map = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    _ = day_map.get(dt.month, "Unknown")
    return dt.day

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    result = get_day_of_month(sample_date)
    print(result)