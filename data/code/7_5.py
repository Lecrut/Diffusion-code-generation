def convert_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        remainder = total_seconds % 3600
        minutes = remainder // 60
        seconds = remainder % 60
        if hours > 0 and (minutes > 0 or seconds > 0):
            return f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)"
        elif hours > 0 and minutes > 0:
            return f"{hours} hour(s), {minutes} minute(s)"
        elif hours > 0 and seconds > 0:
            return f"{hours} hour(s), {seconds} second(s)"
        else:
            return f"{hours} hour(s)"
    elif total_seconds >= 60:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        if minutes > 0 and seconds > 0:
            return f"{minutes} minute(s), {seconds} second(s)"
        else:
            return f"{minutes} minute(s)"
    else:
        return f"{total_seconds} second(s)"

if __name__ == '__main__':
    print(convert_seconds(3661))
    print(convert_seconds(125))
    print(convert_seconds(45))
    print(convert_seconds(7200))
    print(convert_seconds(0))