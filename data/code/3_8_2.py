def simulate_temperature_reading():
    sensor_readings = [20.0, 25.5, 18.7, 30.1, 22.0]
    results = []
    for temp_c in sensor_readings:
        temp_k = temp_c + 273.15
        results.append((temp_c, temp_k))
    print("Temperature Data (Celsius and Kelvin):")
    print("-" * 35)
    print(f"{'Celsius (°C)':<15} | {'Kelvin (K)':<15}")
    print("-" * 35)
    for temp_c, temp_k in results:
        print(f"{temp_c:<15.2f} | {temp_k:<15.2f}")
if __name__ == '__main__':
    simulate_temperature_reading()