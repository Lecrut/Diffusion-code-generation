class TemperatureSensor:
    def __init__(self, sensor_id, temperature_celsius):
        self.sensor_id = sensor_id
        self.temperature_celsius = temperature_celsius

    def to_kelvin(self):
        return self.temperature_celsius + 273.15

    def get_data(self):
        return {
            "sensor_id": self.sensor_id,
            "celsius": self.temperature_celsius,
            "kelvin": self.to_kelvin()
        }

def format_temperature_table(sensors):
    table_data = []
    for sensor in sensors:
        data = sensor.get_data()
        table_data.append(data)

    header = f"{'Sensor ID':<12} {'Celsius (°C)':<15} {'Kelvin (K)':<15}"
    separator = "-" * len(header)
    rows = [header, separator]

    for entry in table_data:
        row = f"{entry['sensor_id']:<12} {entry['celsius']:<15.2f} {entry['kelvin']:<15.2f}"
        rows.append(row)

    return "\n".join(rows)

def main():
    sample_sensors = [
        TemperatureSensor("TH-001", 22.5),
        TemperatureSensor("TH-002", -5.0),
        TemperatureSensor("TH-003", 37.0),
        TemperatureSensor("TH-004", 100.0),
        TemperatureSensor("TH-005", 0.0)
    ]

    table = format_temperature_table(sample_sensors)
    print(table)

if __name__ == '__main__':
    main()