import re
import json
def parse_and_convert(text: str) -> list[dict]:
    pattern = r'(\d+(?:\.\d+)?)\s*(.+?)(m|km|hha)'
    matches = []
    for match in re.finditer(pattern, text):
        value_str = match.group(1).strip()
        unit_str = match.group(2).strip().lower()
        base_unit = match.group(3)
        try:
            numeric_value = float(value_str)
            if 'ha' in unit_str or 'hha' in unit_str:
                converted_val = numeric_value * 100.0 / 4840.0
                final_unit = "ac"
            elif base_unit == "km":
                converted_val = numeric_value * 3280.84
                final_unit = "ft"
            else:
                converted_val = numeric_value
                final_unit = match.group(2).strip().lower() if 'ha' not in unit_str and 'hha' not in unit_str else base_unit
            matches.append({
                "original": text[match.start():match.end()],
                "value": round(converted_val, 4),
                "unit": final_unit
            })
        except ValueError:
            continue
    return matches
if __name__ == '__main__':
    sample_data = [
        "The plot is 5.2 hha.",
        "Distance covered was 10 km.",
        "Room size is 3 meters by 4 meters (total area approx 12 m²).",
        "Field dimensions: 8 ha and 6 hha."
    ]
    results = []
    for item in sample_data:
        parsed_items = parse_and_convert(item)
        if parsed_items:
            results.append({
                "input": item,
                "extracted_measurements": parsed_items
            })
        output_json = json.dumps(results, indent=2)
        print(output_json)