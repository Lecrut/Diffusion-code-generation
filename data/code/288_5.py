import math
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin
if __name__ == '__main__':
    celsius_input_1 = 0.0
    kelvin_output_1 = celsius_to_kelvin(celsius_input_1)
    print(f"Celsius: {celsius_input_1}, Kelvin: {kelvin_output_1}")
    celsius_input_2 = 25.5
    kelvin_output_2 = celsius_to_kelvin(celsius_input_2)
    print(f"Celsius: {celsius_input_2}, Kelvin: {kelvin_output_2}")
    celsius_input_3 = -40.0
    kelvin_output_3 = celsius_to_kelvin(celsius_input_3)
    print(f"Celsius: {celsius_input_3}, Kelvin: {kelvin_output_3}")