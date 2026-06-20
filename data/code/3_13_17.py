def convert_kelvin_to_celsius(readings):
    result = []
    for reading in readings:
        try:
            value = float(reading)
            if value < 0:
                result.append(None)
            else:
                result.append(value - 273.15)
        except (TypeError, ValueError):
            result.append(None)
    return result

if __name__ == '__main__':
    sample_data = [273.15, 0, 300.5, -5, "invalid", 310.0, -274.0, None, 273.15, 100]
    converted = convert_kelvin_to_celsius(sample_data)
    print(converted)