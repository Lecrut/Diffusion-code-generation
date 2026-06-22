def kelvin_to_celsius(readings):
    if readings is None:
        return []
    result = []
    for reading in readings:
        if reading is None:
            result.append(None)
        elif isinstance(reading, (int, float)):
            if reading < 0:
                result.append(None)
            else:
                result.append(reading - 273.15)
        else:
            result.append(None)
    return result

if __name__ == '__main__':
    k_values = [273.15, 300.0, 0, 373.15, -10, None, "bad", 0.0]
    celsius_values = kelvin_to_celsius(k_values)
    print(celsius_values)