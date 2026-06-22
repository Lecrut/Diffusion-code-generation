import datetime

HOLIDAY_CONFIG = {
    "independence_day": {
        "year": 2024,
        "month": 7,
        "day": 4
    }
}

def add_days_to_reference_date(config: dict, days: int) -> str:
    date_info = config["independence_day"]
    base = datetime.date(date_info["year"], date_info["month"], date_info["day"])
    future = base + datetime.timedelta(days=days)
    return future.strftime("%Y-%m-%d")

if __name__ == '__main__':
    result = add_days_to_reference_date(HOLIDAY_CONFIG, 30)
    print(result)