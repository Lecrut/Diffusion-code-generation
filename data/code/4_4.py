class UnitConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    @staticmethod
    def mass_kg_to_lbs(kilograms):
        return kilograms * 2.20462
    @staticmethod
    def mass_lbs_to_kg(pounds):
        return pounds / 2.20462
if __name__ == '__main__':
    print("--- Temperature Conversion ---")
    celsius_sample = 25.0
    fahrenheit_result = UnitConverter.celsius_to_fahrenheit(celsius_sample)
    print(f"{celsius_sample}°C is {fahrenheit_result}°F")
    fahrenheit_sample = 68.0
    celsius_result = UnitConverter.fahrenheit_to_celsius(fahrenheit_sample)
    print(f"{fahrenheit_sample}°F is {celsius_result}°C")
    print("\n--- Mass Conversion ---")
    mass_kg_sample = 10.0
    mass_lbs_result = UnitConverter.mass_kg_to_lbs(mass_kg_sample)
    print(f"{mass_kg_sample} kg is {mass_lbs_result} lbs")
    mass_lbs_sample = 150.0
    mass_kg_result = UnitConverter.mass_lbs_to_kg(mass_lbs_sample)
    print(f"{mass_lbs_sample} lbs is {mass_kg_result} kg")