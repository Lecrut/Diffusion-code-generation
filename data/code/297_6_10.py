def hours_to_milliseconds(hours):
    if not isinstance(hours, (int, float)) or hours < 0:
        raise ValueError("Input must be a non-negative number")
    
    seconds_per_hour = 3600
    milliseconds_per_second = 1000
    total_milliseconds = int(hours * seconds_per_hour * milliseconds_per_second)
    return total_milliseconds

if __name__ == '__main__':
    try:
        sample_hours_1 = 2
        print(f"{sample_hours_1} hours is {hours_to_milliseconds(sample_hours_1)} milliseconds")
        
        sample_hours_2 = 5
        print(f"{sample_hours_2} hours is {hours_to_milliseconds(sample_hours_2)} milliseconds")
        
        invalid_input = -3
        print(hours_to_milliseconds(invalid_input))
    except ValueError as e:
        print(e)