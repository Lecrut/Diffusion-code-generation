def simulate_temperature_reading():
    sensor_readings = {
        "Sensor_A": 20.0,
        "Sensor_B": 25.5,
        "Sensor_C": 15.0,
        "Sensor_D": 30.2
    }
    results = []
    for sensor, celsius in sensor_readings.items():
        kelvin = celsius + 273.15
        results.append({
            "Sensor": sensor,
            "Celsius": celsius,
            "Kelvin": kelvin
        })
    print("Temperature Data Simulation")
    print("--------------------------")
    print("{:<10} {:<10} {:<10}".format("Sensor", "Celsius (°C)", "Kelvin (K)"))
    print("--------------------------")
    for item in results:
        print("{:<10} {:<10.2f} {:<10.2f}".format(
            item["Sensor"], 
            item["Celsius"], 
            item["Kelvin"]
        ))
if __name__ == '__main__':
    simulate_temperature_reading()