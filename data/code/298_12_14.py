from datetime import datetime

def time_difference(time_str1, time_str2):
    format_str = "%H:%M"
    datetime_obj1 = datetime.strptime(time_str1, format_str)
    datetime_obj2 = datetime.strptime(time_str2, format_str)
    
    diff = abs(datetime_obj2 - datetime_obj1)
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    
    return f"{hours} hour(s) and {minutes} minute(s)"

if __name__ == '__main__':
    print(time_difference("14:30", "20:45"))