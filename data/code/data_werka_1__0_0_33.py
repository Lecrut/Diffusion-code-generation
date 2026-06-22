def convert_length(length: float, unit: str) -> float:
    if unit == 'm':
        return length * 3.28084
    elif unit == 'ft':
        return length / 3.28084
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    result_m_to_ft = convert_length(1, 'm')
    print(result_m_to_ft)
    result_ft_to_m = convert_length(1, 'ft')
    print(result_ft_to_m)