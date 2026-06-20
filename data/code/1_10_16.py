import csv
import io

def parse_weight_value(raw_value):
    cleaned = str(raw_value).strip()
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None

def aggregate_weights_from_csv_string(csv_content):
    valid_weights = []
    reader = csv.reader(io.StringIO(csv_content))
    for row in reader:
        for cell in row:
            parsed_weight = parse_weight_value(cell)
            if parsed_weight is not None:
                valid_weights.append(parsed_weight)
    return valid_weights

def compute_average_weight(weights_list):
    if not weights_list:
        return 0.0
    total_sum = sum(weights_list)
    count = len(weights_list)
    return total_sum / count

def get_weight_statistics(csv_data):
    collected_weights = aggregate_weights_from_csv_string(csv_data)
    average_value = compute_average_weight(collected_weights)
    return {
        "weights": collected_weights,
        "count": len(collected_weights),
        "average": average_value
    }

if __name__ == '__main__':
    sample_csv_data = """item,weight,note
scale1,10.5,valid
scale2,bad_entry,invalid
scale3,20.0,valid
scale4,,missing
scale5,15.5,valid
"""
    result = get_weight_statistics(sample_csv_data)
    print(result["average"])
    print(result["count"])
    print(result["weights"])