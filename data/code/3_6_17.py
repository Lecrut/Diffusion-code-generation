def process_temperature_data(sensor_data):
    processed_data = []
    for sensor_id, temp_celsius in sensor_data.items():
        temp_kelvin = temp_celsius + 273.15
        processed_data.append({
            'sensor_id': sensor_id,
            'celsius': temp_celsius,
            'kelvin': temp_kelvin
        })
    return processed_data

def format_temperature_table(processed_data):
    header = "{:<10} | {:<10} | {:<10}".format("Sensor ID", "Celsius", "Kelvin")
    separator = "-" * len(header)
    table_rows = [header, separator]
    for entry in processed_data:
        row = "{:<10} | {:<10.2f} | {:<10.2f}".format(
            entry['sensor_id'],
            entry['celsius'],
            entry['kelvin']
        )
        table_rows.append(row)
    return "\n".join(table_rows)

if __name__ == '__main__':
    sample_sensor_data = {
        "S001": 22.5,
        "S002": -5.0,
        "S003": 37.2,
        "S004": 0.0,
        "S005": 100.0
    }

    processed = process_temperature_data(sample_sensor_data)
    table = format_temperature_table(processed)
    print(table)