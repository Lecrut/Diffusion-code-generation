class TemperatureSensor:
    def __init__(self, name, celsius_value):
        self.name = name
        self.celsius_value = celsius_value

    def to_kelvin(self):
        return self.celsius_value + 273.15

    def __repr__(self):
        return f"Sensor(name='{self.name}', celsius={self.celsius_value})"

def process_sensors(sensors):
    results = []
    for sensor in sensors:
        kelvin = sensor.to_kelvin()
        results.append({
            'name': sensor.name,
            'celsius': sensor.celsius_value,
            'kelvin': kelvin
        })
    return results

def format_table(data):
    name_col_max = max(len(row['name']) for row in data) + 2
    celsius_col_max = 10
    kelvin_col_max = 10

    header = f"{'Sensor':<{name_col_max}}{'Celsius':>{celsius_col_max}}{'Kelvin':>{kelvin_col_max}}"
    separator = "-" * len(header)
    lines = [header, separator]

    for row in data:
        line = f"{row['name']:<{name_col_max}}{row['celsius']:>{celsius_col_max}.2f}{row['kelvin']:>{kelvin_col_max}.2f}"
        lines.append(line)

    return "\n".join(lines)

def main():
    sample_sensors = [
        TemperatureSensor("Lab A", 20.5),
        TemperatureSensor("Lab B", -5.0),
        TemperatureSensor("Server Room", 32.1),
        TemperatureSensor("Outdoor", -15.3),
        TemperatureSensor("Greenhouse", 28.7)
    ]

    data = process_sensors(sample_sensors)
    table = format_table(data)
    print(table)

if __name__ == '__main__':
    main()