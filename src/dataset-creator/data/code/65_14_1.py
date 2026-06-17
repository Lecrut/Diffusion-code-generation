import re
import json
def parse_and_convert(text: str) -> list[dict]:
    pattern = r'(\d+(?:\.\d+)?)\s*(cm|km|m|mm)'
    matches = []
    for match in re.finditer(pattern, text):
        value_str = match.group(1).replace(',', '.')
        unit = match.group(2)
        try:
            number = float(value_str)
        except ValueError:
            continue
        converted_value = 0.0
        if 'km' in unit:
            converted_value = number * 1e3
        elif 'mm' in unit:
            converted_value = number / 1e-3
        else:
            converted_value = number
        matches.append({
            "original": match.group(0),
            "value": round(converted_value, 4)
        })
    return matches
if __name__ == '__main__':
    sample_data = [
        "The room is 3.5 meters wide.",
        "Distance: 2 km and height: 150 cm",
        "Lengths: 10mm, 5cm, 0.7km"
    ]
    results = []
    for text in sample_data:
        parsed_values = parse_and_convert(text)
        if not parsed_values:
            continue
        result_entry = {
            "input_text": text,
            "converted_measurements": [item["value"] for item in parsed_values]
        }
        results.append(result_entry)
    output_json = json.dumps(results, indent=2)
    print(output_json)