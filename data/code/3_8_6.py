import pandas as pd
def simulate_temperature_reading():
    sensor_readings = {
        "Sensor_A": 25.0,
        "Sensor_B": 30.5,
        "Sensor_C": 15.2,
        "Sensor_D": 22.8
    }
    data = []
    for sensor, celsius in sensor_readings.items():
        kelvin = celsius + 273.15
        data.append({
            "Sensor": sensor,
            "Celsius": celsius,
            "Kelvin": kelvin
        })
    df = pd.DataFrame(data)
    print("Temperature Data Simulation")
    print("-------------------------")
    print(df.to_string(index=False))
if __name__ == '__main__':
    simulate_temperature_reading()