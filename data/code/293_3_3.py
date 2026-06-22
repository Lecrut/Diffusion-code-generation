class UnitConverter:

    def kg_to_pounds(self, kg):
        return kg * 2.20462

    def pounds_to_kg(self, pounds):
        return pounds / 2.20462

    def kg_to_ounces(self, kg):
        return kg * 35.274

    def ounces_to_kg(self, ounces):
        return ounces / 35.274
if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kg_to_pounds(1))
    print(converter.pounds_to_kg(2.20462))
    print(converter.kg_to_ounces(1))
    print(converter.ounces_to_kg(35.274))