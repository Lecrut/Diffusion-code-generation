from datetime import datetime
def get_weekday(date_str: str) -> int:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.weekday()
if __name__ == '__main__':
    samples = ["2023-10-05", "2024-06-15"]
    for s in samples:
        print(get_weekday(s))