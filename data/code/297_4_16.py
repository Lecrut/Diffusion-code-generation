def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    temp_c = 0.0
    try:
        temp_f = celsius_to_fahrenheit(temp_c)
        print(f"{temp_c}°C is {temp_f}°F")
    except TypeError as e:
        print(f"Error: {e}")

    temp_c_error = -100
    try:
        temp_f_error = celsius_to_fahrenheit(temp_c_error)
        print(f"{temp_c_error}°C is {temp_f_error}°F")
    except TypeError as e:
        print(f"Error: {e}")