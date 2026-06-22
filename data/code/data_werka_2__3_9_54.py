def kelvin_to_celsius(kelvin_list):
    def convert(temp):
        if not isinstance(temp, (int, float)):
            return None
        if temp < 0:
            return None
        return temp - 273.15

    return [convert(temp) for temp in kelvin_list]

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 400, -10, 'abc', None]
    converted_values = kelvin_to_celsius(sample_kelvin_values)
    print(converted_values)