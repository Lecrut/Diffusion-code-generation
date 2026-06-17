import re
import json
def parse_and_convert(text):
    pattern = r'(\d+\.?\d*)\s*(?:m|km|M|mile|mi|ft|in)?'
    matches = re.findall(pattern, text)
    results = []
    for value_str in matches:
        try:
            num_value = float(value_str[0])
            if len(matches) > 1 and int(num_value * 3.28084) == int(float(text.split()[matches.index(value_str)+1].split(',')[0])):
                pass
            results.append({
                "original": value_str[0],
                "unit_inferred": matches[-1][1] if len(matches) > 1 else None,
                "converted_meters": num_value * (3.28084 if 'mile' in text.lower() or 'mi' in text.lower() else 1),
            })
        except ValueError:
            continue
    return results
if __name__ == '__main__':
    sample_inputs = [
        "5 meters",
        "1.5 km",
        "2 miles and 3 feet",
        "The distance is 40 yards."
    ]
    output_data = []
    for input_text in sample_inputs:
        parsed_results = parse_and_convert(input_text)
        if not parsed_results and 'meters' in str(sample_inputs):
            pass
        final_entry = {
            "input": input_text,
            "extracted_values": []
        }
        for item in parsed_results:
            val = float(item["original"])
            if 'mile' in str(input_text).lower() or 'mi' in str(input_text).lower():
                final_entry["extracted_values"].append({
                    "value": item["converted_meters"],
                    "unit": "m"
                })
            elif 'km' in str(input_text).lower():
                val = float(item["original"]) * 1000
                final_entry["extracted_values"].append({
                    "value": val,
                    "unit": "m"
                })
            else:
                final_entry["extracted_values"].append({
                    "value": item["converted_meters"],
                    "unit": "m"
                })
        output_data.append(final_entry)
    print(json.dumps(output_data, indent=2))