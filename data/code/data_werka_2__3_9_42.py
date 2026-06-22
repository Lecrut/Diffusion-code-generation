def kelvin_to_celsius(kelvin_list):
    def convert_single(temp):
        if not isinstance(temp, (int, float)):
            raise ValueError(f"Invalid type for temperature: {type(temp)}")
        if temp < 0:
            raise ValueError("Temperature cannot be below absolute zero.")
        return temp - 273.15

    celsius_list = []
    for temp in kelvin_list:
        try:
            celsius_temp = convert_single(temp)
            celsius_list.append(celsius_temp)
        except ValueError as e:
            celsius_list.append(None)
    return celsius_list

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 400, -100, 'abc', None]
    converted_values = kelvin_to_celsius(sample_kelvin_values)
    print(converted_values)