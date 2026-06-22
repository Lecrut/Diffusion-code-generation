def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Invalid unit. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    sample_value_m = 10
    sample_value_ft = 32.8084
    result_m_to_ft = convert_length(sample_value_m, 'm')
    result_ft_to_m = convert_length(sample_value_ft, 'ft')
    print(result_m_to_ft)
    print(result_ft_to_m)