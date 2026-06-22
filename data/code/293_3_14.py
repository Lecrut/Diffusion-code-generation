class UnitConverter:
    def kg_to_lb(self, kg):
        return kg * 2.20462

    def lb_to_kg(self, lb):
        return lb / 2.20462

    def kg_to_oz(self, kg):
        return kg * 35.274

    def oz_to_kg(self, oz):
        return oz / 35.274

if __name__ == '__main__':
    converter = UnitConverter()
    print(f"1 kg is {converter.kg_to_lb(1):.2f} lbs")
    print(f"2.20462 lbs is {converter.lb_to_kg(2.20462):.2f} kgs")
    print(f"1 kg is {converter.kg_to_oz(1):.2f} ozs")
    print(f"35.274 ozs is {converter.oz_to_kg(35.274):.2f} kgs")