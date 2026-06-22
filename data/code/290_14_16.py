class MassConverter:
    def kg_to_lb(self, kg):
        return round(kg * 2.20462, 2)
    
    def lb_to_kg(self, lb):
        return round(lb / 2.20462, 2)

if __name__ == '__main__':
    converter = MassConverter()
    print(f"1 kg is approximately {converter.kg_to_lb(1)} pounds.")
    print(f"5 kg is approximately {converter.kg_to_lb(5)} pounds.")
    print(f"2.2 pounds is approximately {converter.lb_to_kg(2.2)} kilograms.")
    print(f"11.02 pounds is approximately {converter.lb_to_kg(11.02)} kilograms.")