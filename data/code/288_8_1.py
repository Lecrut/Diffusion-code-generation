import random
def get_temperature():
    return random.uniform(10.0, 35.0)
def display_temperature(temp, scale):
    if scale == "Celsius":
        print(f"Temperature: {temp:.2f}°C")
    elif scale == "Fahrenheit":
        fahrenheit = (temp * 9/5) + 32
        print(f"Temperature: {fahrenheit:.2f}°F")
    elif scale == "Kelvin":
        kelvin = temp + 273.15
        print(f"Temperature: {kelvin:.2f}K")
if __name__ == '__main__':
    sample_temp = get_temperature()
    available_scales = ["Celsius", "Fahrenheit", "Kelvin"]
    chosen_scale = random.choice(available_scales)
    print("--- Temperature Converter Simulation ---")
    print(f"Sample temperature generated: {sample_temp:.2f} (in a base scale)")
    print(f"You have selected the viewing scale: {chosen_scale}")
    print("-" * 35)
    display_temperature(sample_temp, chosen_scale)