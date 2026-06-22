from datetime import datetime

def time_difference(time_str1: str, time_str2: str) -> str:
    format_str = "%H:%M"
    time_obj1 = datetime.strptime(time_str1, format_str)
    time_obj2 = datetime.strptime(time_str2, format_str)
    
    diff = abs((time_obj2 - time_obj1).seconds // 3600)
    minutes = abs((time_obj2 - time_obj1).seconds // 60) % 60
    
    return f"{diff} hours and {minutes} minutes"

if __name__ == '__main__':
    print(time_difference("14:30", "18:45"))