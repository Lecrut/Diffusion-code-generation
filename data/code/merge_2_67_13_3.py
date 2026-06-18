import sys
def convert_temperature(celsius_list):
    fahrenheit = [c * 9 / 5 + 32 for c in celsius_list]
    kelvin = [c + 273.15 for c in celsius_list]
    return {'fahrenheit': fahrenheit, 'kelvin': kelvin}
def main():
    raw_data = [[-40, -20, 0, 20], [-10, 10, 30]]
    results_map = {}
    for batch in raw_data:
        converted = convert_temperature(batch)
        scale_name = 'celsius' if len(batch) > 0 else None
        results_map[scale_name] = {**converted}
if __name__ == '__main__':
    main()