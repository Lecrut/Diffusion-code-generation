def kelvin_to_celsius(temperatures):
    celsius_list = []
    for temp in temperatures:
        if isinstance(temp, (int, float)):
            if temp < 0:
                celsius_list.append(None)
            else:
                celsius_list.append(temp - 273.15)
        else:
            celsius_list.append(None)
    return celsius_list

if __name__ == '__main__':
    sample_data = [0, 273.15, 373.15, 1000, -10, "invalid", 0.0]
    result = kelvin_to_celsius(sample_data)
    print(result)