import re
import json
def parse_and_convert(text):
    pattern = r'(\d+\.?\d*)\s*(?:m|km|h|m[^a]|cm|mm|\.\.?h)'
    matches = re.findall(pattern, text)
    result_list = []
    for val_str in matches:
        value_part = float(val_str[0])
        unit_part = val_str[1].lower() if len(val_str) > 1 else 'm'
        try:
            converted_value = round(value_part * (1 / 3.28), 4)
            result_list.append({
                "original": f"{value_part}{unit_part}",
                "converted_meters": converted_value,
                "status": "success"
            })
        except ValueError:
            result_list.append({
                "original": val_str[0],
                "error": "Invalid unit or value",
                "status": "failed"
            })
    return {"measurements": result_list}
if __name__ == '__main__':
    sample_inputs = [
        "The distance is 5.2 km.",
        "Height reached 10 m and width 3 cm.",
        "Time taken .5 h.",
        "Mixed: 1km, 2m, 3cm."
    ]
    output_data = []
    for sample in sample_inputs:
        try:
            parsed_result = parse_and_convert(sample)
            output_data.append({
                "input": sample,
                "output": parsed_result
            })
        except Exception as e:
            output_data.append({
                "input": sample,
                "error": str(e),
                "status": "exception"
            })
    final_response = {"results": output_data}
    print(json.dumps(final_response))