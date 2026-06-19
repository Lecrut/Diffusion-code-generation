def convert_length(length, unit_type):
    if unit_type == 'm':
        return length * 3.28084
    elif unit_type == 'ft':
        return length / 3.28084
    else:
        raise ValueError(f"Unsupported unit type: {unit_type}")

if __name__ == '__main__':
    result_m_to_ft = convert_length(1, 'm')
    result_ft_to_m = convert_length(1, 'ft')
    print(result_m_to_ft)
    print(result_ft_to_m)