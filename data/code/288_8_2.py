import random
def get_temperature():
    temp = random.randint(0, 100)
    return temp
def display_temperature(temp, scale):
    if scale == "celsius":
        print(f"Temperature: {temp}°C")
    elif scale == "fahrenheit":
        print(f"Temperature: {((temp * 9/5) + 32):.2f}°F")
    elif scale == "kelvin":
        print(f"Temperature: {temp + 273.15}°K")
    else:
        print("Invalid scale selected.")
if __name__ == '__main__':
    sample_temperature = get_temperature()
    available_scales = ["celsius", "fahrenheit", "kelvin"]
    selected_scale = random.choice(available_scales)
    display_temperature(sample_temperature, selected_scale)