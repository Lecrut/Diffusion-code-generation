def simulate_temperature_reading():
    sensor_readings = {
        "Sensor_A": 25.0,
        "Sensor_B": 300.15,
        "Sensor_C": 15.5,
        "Sensor_D": 293.15
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
    print("-------------------------")
    print("{:<10} | {:<10} | {:<10}".format("Sensor", "Celsius (°C)", "Kelvin (K)"))
    print("------------|------------|------------")
    for item in results:
        print("{:<10} | {:<10.2f} | {:<10.2f}".format(
            item["Sensor"], 
            item["Celsius"], 
            item["Kelvin"]
        ))
if __name__ == '__main__':
    simulate_temperature_reading()