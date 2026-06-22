def hours_to_time(hours):
    if not isinstance(hours, (int, float)) or hours < 0:
        raise ValueError("Hours must be a non-negative number")
    
    minutes = int(hours * 60)
    seconds = int((hours * 3600) % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    print(hours_to_time(1.5))