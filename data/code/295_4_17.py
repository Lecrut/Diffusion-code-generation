class WeightConverter:
    def kg_to_lb(self, kilograms):
        return round(kilograms * 2.20462, 3)

if __name__ == '__main__':
    converter = WeightConverter()
    weight_in_kg = 10.0
    weight_in_lb = converter.kg_to_lb(weight_in_kg)
    print(f"{weight_in_kg} kilograms is equal to {weight_in_lb} pounds")