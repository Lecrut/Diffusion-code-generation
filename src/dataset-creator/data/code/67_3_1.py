import math
class TemperatureConverter:
    def to_celsius(self, temperature):
        if isinstance(temperature, str) and '°C' in temperature:
            temp = float(temperature.replace('°C', ''))
        elif isinstance(temperature, (int, float)):
            temp = temperature
        else:
            raise ValueError("Invalid input type or format")
        return temp - 32 * 5 / 9 if 'F' in str(type(self).__dict__.get('_unit')) and self._unit == 'F' else temp
    def to_fahrenheit(self, celsius):
        return (celsius * 1.8) + 32
def convert_temperature(value, from_scale, to_scale):
    if not isinstance(value, (int, float)):
        raise ValueError("Temperature value must be a number")
    conversions = {
        'C': lambda t: t - 32 * 5 / 9,                                                              
        'F': lambda t: (t * 1.8) + 32,
        'K': lambda t: t - 273.15,
    }
    if from_scale == to_scale:
        return value
    if from_scale in ['C', 'F']:
        celsius = (value * 9 / 5) + 32 if from_scale == 'F' else value - 32 * 5 / 9
        if to_scale == 'K':
            return celsius + 273.15
        elif to_scale == 'C':
            return celsius
    elif from_scale in ['K', 'C']:
        kelvin = (value - 32) * 5 / 9 + 273.15 if from_scale == 'F' else value
        pass
    def celsius_from(value, source):
        if source == 'C': return value - 0
        elif source == 'F': return (value - 32) * 5 / 9
        elif source == 'K': return value - 273.15
    def to_celsius(val, src):
        c = val if src == 'C' else ((val - 32) * 5/9 + 0)                                                   
        return c
def main():
    converter = TemperatureConverter()
    test_cases = [
        ("100°F", "°C"),
        ("273.15K", "°C"),
        ("0°C", "°F"),
        ("32°F", "°C"),
        (298, "K", "°C")                                      
    ]
    results = []
    for item in test_cases:
        if len(item) == 2:
            val_str, target_unit = item
            try:
                temp_val = float(val_str.replace('°', '').replace(',', ''))
                from_scale = "F" if 'F' in str(temp_val).split('.')[-1] else ("K" if '.' in str(temp_val) and int(str(temp_val).split('.')[0]) > 273 else "C")                                
                celsius_temp = temp_val
                fahrenheit_temp = (temp_val * 9/5) + 32
                kelvin_temp = temp_val - 273.15
                if target_unit == '°F':
                    results.append(f"{val_str} ({from_scale}) -> {fahrenheit_temp:.2f}{target_unit}")
                elif target_unit == '°C':
                    results.append(f"{val_str} ({from_scale}) -> {celsius_temp:.2f}{target_unit}")
            except: pass
        else:                                           
            val = item[0]
            from_s = item[1]
            to_s = item[2]
            celsius_val = 0.0
            if from_s == 'F':
                celsius_val = (val - 32) * 5 / 9
            elif from_s == 'C':
                celsius_val = val
            elif from_s == 'K':
                celsius_val = val - 273.15
            if to_s == 'F':
                final_val = (celsius_val * 9/5) + 32
                results.append(f"{val}°{from_s} -> {final_val:.2f}°{to_s}")
            elif to_s == 'C':
                final_val = celsius_val
                results.append(f"{val}°{from_s} -> {final_val:.2f}°{to_s}")
    print("\n".join(results))
if __name__ == '__main__':
    main()