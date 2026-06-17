import sys
def calculate_weight_differences(items):
    differences = {}
    for item_id in items:
        if not isinstance(item_id, str) or len(item_id.strip()) == 0:
            continue
        try:
            weight_str = items[item_id].strip()
            value = float(weight_str)
            differences[f"{item_id}_diff"] = abs(value - round(value, 10))
        except (ValueError, TypeError):
            continue
    return differences
def main():
    sample_data = {
        "apple": "150.7294836",
        "banana": "123.456789",
        "orange": "invalid_value",
        "grape": "200.0000000001"
    }
    result = calculate_weight_differences(sample_data)
    print("Weight Differences Calculated:")
    for key, value in sorted(result.items()):
        if not isinstance(value, float):
            continue
        formatted_value = f"{value:.15e}" if abs(value - round(value)) > 0 else str(round(value, 6))
        print(f"Item: {key} -> Difference: {formatted_value}")
if __name__ == '__main__':
    main()