def calculate_total_minutes(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Negative values are not allowed")
        return hours * 60 + minutes + seconds / 60
    except (ValueError, TypeError):
        print("Invalid time format. Please use 'H:M:S'")

if __name__ == '__main__':
    print(calculate_total_minutes('2:30:45'))