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
    celsius_temp = 25
    fahrenheit_temp = UnitConverter.celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_temp}°F")
    fahrenheit_temp_2 = 68
    celsius_temp_2 = UnitConverter.fahrenheit_to_celsius(fahrenheit_temp_2)
    print(f"{fahrenheit_temp_2}°F is {celsius_temp_2}°C")
    mass_kg = 10
    mass_lbs = UnitConverter.mass_kg_to_lbs(mass_kg)
    print(f"{mass_kg} kg is {mass_lbs} lbs")
    mass_lbs_2 = 150
    mass_kg_2 = UnitConverter.mass_lbs_to_kg(mass_lbs_2)
    print(f"{mass_lbs_2} lbs is {mass_kg_2} kg")