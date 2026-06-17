from datetime import timedelta
def add_years(date_str: str, years: int) -> str:
    date_obj = __import__('datetime').date.fromisoformat(date_str)
    return (date_obj + timedelta(days=years * 365)).isoformat()
if __name__ == '__main__':
    result = add_years("2024-01-01", 5)
    print(result)