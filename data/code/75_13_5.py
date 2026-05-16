from datetime import datetime
def date_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    diff = date2 - date1
    years = diff.days // 365
    remaining_days = diff.days % 365
    months = remaining_days // 30
    remaining_days = remaining_days % 30
    days = diff.days % 30
    parts = []
    if years > 0:
        parts.append(f"{years} years")
    if months > 0:
        parts.append(f"{months} months")
    if days > 0:
        if len(parts) == 0:
            parts.append(f"{days} days")
        else:
            parts.append(f"{days} days")
    if not parts:
        return "0 days"
    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    else:
        return ", ".join(parts[:-1]) + f", and {parts[-1]}"
if __name__ == '__main__':
    date1 = "2023-01-15"
    date2 = "2024-05-20"
    result = date_difference(date1, date2)
    print(result)