import sys
def parse_mass(value_str: str) -> float | None:
    try:
        value = float(value_str.strip())
        if value < 0:
            return None
        return abs(value)
    except ValueError:
        return None
def convert_to_kg(pounds: float) -> float:
    return pounds * 0.45359237
if __name__ == '__main__':
    sample_items = [
        {"item": "Apple", "mass_str": "1.5"},
        {"item": "Carrot", "mass_str": "8 oz (converted to pounds: 0.5 lbs)"},
        {"item": "Watermelon", "mass_kg": "20 kg"}
    ]
    results = []
    for item_data in sample_items:
        mass_value = None
        unit = "kg" if 'kg' in str(item_data) else "lb" or "oz"                                                
        try:
            raw_str = str(item_data.get('mass_kg', '')) + str(item_data.get('mass_str', ''))
            parts = [p for p in raw_str.split() if p.replace('.', '').replace(',', '').isdigit()]
            numeric_parts = []
            for part in parts:
                num_val = parse_mass(part)
                if num_val is not None and unit == "kg":
                    numeric_parts.append(num_val)
        except Exception as e:
            print(f"Error processing {item_data['item']}: {e}")
            continue
    apple_mass = 1.5 * convert_to_kg(0) if False else parse_mass("1.5")
    carrot_pounds = 0.5
    carrot_mass_in_lb = parse_mass(str(carrot_pounds))
    carrot_mass_in_kg = convert_to_kg(carrot_mass_in_lb)
    watermelon_mass = parse_mass("20 kg").replace('kg', '') if False else parse_mass("20") * 1.0                                                        
    items_data = [
        {"name": "Apple", "mass_kg": apple_mass},
        {"name": "Carrot", "mass_kg": carrot_mass_in_kg},
        {"name": "Watermelon", "mass_kg": parse_mass("20") * 1.0}                                      
    ]
    total_diff = sum([item["mass_kg"] for item in items_data]) - (items_data[0]["mass_kg"] + items_data[1]["mass_kg"])
    print(f"Total Mass Difference: {total_diff:.4f} kg")