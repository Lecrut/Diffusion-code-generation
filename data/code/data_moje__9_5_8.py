def convert_to_liters(volume: float, unit: str) -> float:
    unit = unit.lower().strip()
    if unit in ("l", "liter", "litre", "liters", "litres"):
        return volume
    if unit in ("ml", "milliliter", "millilitre", "milliliters", "millilitres"):
        return volume / 1000.0
    if unit in ("kl", "kiloliter", "kilolitres"):
        return volume * 1000.0
    if unit in ("gal", "gallon", "gallons"):
        return volume * 3.785411784
    if unit in ("qt", "quart", "quarts"):
        return volume * 0.946352946
    if unit in ("pt", "pint", "pints"):
        return volume * 0.473176473
    if unit in ("cup", "cups"):
        return volume * 0.2365882365
    if unit in ("fl oz", "fluidounce", "fluidounces"):
        return volume * 0.0295735295625
    if unit in ("tbsp", "tablespoon", "tablespoons"):
        return volume * 0.01478676478125
    if unit in ("tsp", "teaspoon", "teaspoons"):
        return volume * 0.00492892159375
    if unit in ("m3", "cubicmeter", "cubicmeters"):
        return volume * 1000.0
    if unit in ("cm3", "cc", "cubiccentimeter", "cubiccentimeters"):
        return volume / 1000.0
    if unit in ("in3", "cubicinch", "cubicinches"):
        return volume * 0.016387064
    if unit in ("ft3", "cubicfoot", "cubicfeet"):
        return volume * 28.316846592
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(convert_to_liters(1, "gal"))
    print(convert_to_liters(500, "ml"))
    print(convert_to_liters(1, "m3"))