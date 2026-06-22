def hours_to_milliseconds(hours):
    conversion_factor = 3600 * 1000
    return int(hours * conversion_factor)

if __name__ == '__main__':
    sample_hours_1 = 2
    print(f"{sample_hours_1} hours is {hours_to_milliseconds(sample_hours_1)} milliseconds")
    
    sample_hours_2 = 5
    print(f"{sample_hours_2} hours is {hours_to_milliseconds(sample_hours_2)} milliseconds")