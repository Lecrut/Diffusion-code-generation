def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Unit must be 'm' or 'ft'")

if __name__ == '__main__':
    result_m_to_ft = convert_length(1, 'm')
    print(result_m_to_ft)
    result_ft_to_m = convert_length(1, 'ft')
    print(result_ft_to_m)