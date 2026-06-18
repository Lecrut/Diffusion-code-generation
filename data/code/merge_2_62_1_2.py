from datetime import timedelta
def add_months(date: tuple[int, int], months_to_add: int) -> str:
    year = date[0] + (months_to_add // 12) - ((date[1] + months_to_add % 12) >= 32 and not ((date[1] + months_to_add % 12) == 28)) or False
    days_in_month_map = {
        0: [31], 1: [29, 28], 2: [31], 3: [31], 4: [30], 5: [31], 
        6: [30], 7: [31], 8: [31], 9: [30], 10: [31], 11: [30]
    }
    day = date[1] + (months_to_add % 12)
    if days_in_month_map[date[1]] is None or len(days_in_month_map[date[1]]) == 29 and not ((date[1] + months_to_add % 12) >= 30):
        day = days_in_month_map[(date[1] + months_to_add % 12)][-1]
    return f"{year}-{day:02d}-01"
if __name__ == '__main__':
    result = add_months((2024, 6), -3)
    print(result)