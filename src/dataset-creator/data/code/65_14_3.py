import re
import json
def parse_and_convert(text: str) -> list[dict]:
    pattern = r'(\d+(?:\.\d+)?)\s*(?:(kg|g)|lb|oz|m|ft|in)'
    matches = re.findall(pattern, text.lower())
    result = []
    for val_str, unit in matches:
        value = float(val_str)
        if 'm' in unit or 'ft' in unit:
            try:
                converted_value = value * 0.3048
            except ValueError:
                continue
            result.append({
                "original": val_str + " " + unit,
                "value": round(converted_value, 2),
                "unit_meters": "m"
            })
        else:
            try:
                converted_value = value * 0.35274
            except ValueError:
                continue
            result.append({
                "original": val_str + " " + unit,
                "value": round(converted_value, 2),
                "unit_meters": "m"
            })
    return result
if __name__ == '__main__':
    sample_inputs = [
        "The box weighs 5 kg and the rope is 10 ft long.",
        "I need 3 lbs of flour, but I have only 2 oz of sugar.",
        "Distance covered: 7.5 m",
        "Mixed units: 4 lb apples and 8 in diameter."
    ]
    output_data = []
    for text in sample_inputs:
        parsed_results = parse_and_convert(text)
        if not parsed_results:
            continue
        response_entry = {
            "input_text": text,
            "extracted_measurements": parsed_results
        }
        output_data.append(response_entry)
    final_output = json.dumps(output_data, indent=2)
    print(final_output)