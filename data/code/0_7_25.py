def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Unit must be 'm' or 'ft'")

if __name__ == '__main__':
    meters = 10
    feet = convert_length(meters, 'm')
    print(f"{feet}")
    
    feet_val = 32.8084
    meters_back = convert_length(feet_val, 'ft')
    print(f"{meters_back}")