if __name__ == '__main__':
    temperatures_celsius = [0.0, 10.0, 25.0, 37.0, 100.0]
    for temp_c in temperatures_celsius:
        temp_f = (temp_c * 9/5) + 32
        temp_k = temp_c + 273.15
        print(f"Celsius: {temp_c:.2f}, Fahrenheit: {temp_f:.2f}, Kelvin: {temp_k:.2f}")