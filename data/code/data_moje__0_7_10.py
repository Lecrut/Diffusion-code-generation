def convert_length(value, unit_type):
    if unit_type == 'm':
        return value * 3.28084
    elif unit_type == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Invalid unit type. Use 'm' or 'ft'.")

if __name__ == '__main__':
    result_m_to_ft = convert_length(10, 'm')
    print(result_m_to_ft)
    result_ft_to_m = convert_length(32.8084, 'ft')
    print(result_ft_to_m)