def convert_hours_to_time(hours):
    if not isinstance(hours, (int, float)) or hours < 0:
        raise ValueError("Input must be a non-negative number representing hours")
    
    minutes = int(hours * 60)
    seconds = int((hours * 3600) % 60)
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    print(convert_hours_to_time(1.5))
    print(convert_hours_to_time(0))
    print(convert_hours_to_time(2.75))