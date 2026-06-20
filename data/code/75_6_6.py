import datetime

def date_difference(date1: str, date2: str) -> tuple:
    try:
        format_str = "%Y-%m-%d"
        date1_obj = datetime.datetime.strptime(date1, format_str)
        date2_obj = datetime.datetime.strptime(date2, format_str)
        
        diff = abs(date2_obj - date1_obj)
        total_seconds = int(diff.total_seconds())
        
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        return hours, minutes, seconds
    except ValueError:
        raise ValueError("Input dates must be in the format 'YYYY-MM-DD'")

if __name__ == '__main__':
    result1 = date_difference("2023-01-01", "2023-01-10")
    print(f"Hours: {result1[0]}, Minutes: {result1[1]}, Seconds: {result1[2]}")
    
    result2 = date_difference("2024-05-15", "2024-04-01")
    print(f"Hours: {result2[0]}, Minutes: {result2[1]}, Seconds: {result2[2]}")