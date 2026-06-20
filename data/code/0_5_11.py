class UnitConverter:
    def __init__(self):
        self.base_units = {}
        self.conversion_factors = {}

    def add_unit(self, unit_name, factor_to_base):
        self.base_units[unit_name] = factor_to_base
        self.conversion_factors[unit_name] = factor_to_base

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {to_unit}")

        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]

        base_value = value * factor_from
        result = base_value / factor_to
        return result

    def convert_arbitrary(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        path = self._find_conversion_path(from_unit, to_unit)
        if path is None:
            raise ValueError(f"No conversion path from {from_unit} to {to_unit}")

        result = value
        for i in range(len(path) - 1):
            current = path[i]
            next_unit = path[i + 1]
            result = self.convert(result, current, next_unit)
        return result

    def _find_conversion_path(self, start, end):
        if start == end:
            return [start]
        if start not in self.conversion_factors or end not in self.conversion_factors:
            return None

        visited = set()
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            current = path[-1]
            if current == end:
                return path
            if current in visited:
                continue
            visited.add(current)
            for next_unit in self.conversion_factors:
                if next_unit not in visited:
                    queue.append(path + [next_unit])
        return None

if __name__ == '__main__':
    converter = UnitConverter()
    converter.add_unit('meter', 1.0)
    converter.add_unit('kilometer', 1000.0)
    converter.add_unit('centimeter', 0.01)
    converter.add_unit('millimeter', 0.001)
    converter.add_unit('mile', 1609.34)
    converter.add_unit('yard', 0.9144)
    converter.add_unit('foot', 0.3048)
    converter.add_unit('inch', 0.0254)

    result1 = converter.convert(5, 'kilometer', 'meter')
    print(result1)

    result2 = converter.convert(1, 'mile', 'kilometer')
    print(result2)

    result3 = converter.convert(100, 'centimeter', 'inch')
    print(result3)

    result4 = converter.convert_arbitrary(2.5, 'foot', 'millimeter')
    print(result4)

    result5 = converter.convert(0.5, 'kilometer', 'foot')
    print(result5)

    result6 = converter.convert(72, 'inch', 'centimeter')
    print(result6)

    result7 = converter.convert(1, 'yard', 'mile')
    print(result7)

    result8 = converter.convert(3, 'meter', 'kilometer')
    print(result8)

    result9 = converter.convert(1500, 'millimeter', 'centimeter')
    print(result9)

    result10 = converter.convert_arbitrary(1, 'inch', 'kilometer')
    print(result10)