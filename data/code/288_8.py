import random
def get_temperature():
    return random.uniform(10.0, 35.0)
def display_temperature(temp, scale):
    if scale == "Celsius":
        print(f"Temperature: {temp:.2f}°C")
    elif scale == "Fahrenheit":
        celsius = (temp * 9/5) + 32
        print(f"Temperature: {celsius:.2f}°F")
    elif scale == "Kelvin":
        kelvin = temp + 273.15
        print(f"Temperature: {kelvin:.2f}K")
    else:
        print("Invalid scale selected.")
if __name__ == '__main__':
    sample_temperature = get_temperature()
    available_scales = ["Celsius", "Fahrenheit", "Kelvin"]
    selected_scale = random.choice(available_scales)
    print("--- Temperature Converter Simulation ---")
    print(f"Sample Temperature Generated: {sample_temperature:.2f}")
    print(f"Viewing in Scale: {selected_scale}")
    display_temperature(sample_temperature, selected_scale)