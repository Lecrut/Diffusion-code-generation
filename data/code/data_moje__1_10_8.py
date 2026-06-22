import csv
import io

def parse_weights_from_csv(csv_text):
    parsed_values = []
    text_stream = io.StringIO(csv_text)
    reader = csv.reader(text_stream)
    for row in reader:
        for item in row:
            cleaned_item = item.strip()
            if not cleaned_item:
                continue
            try:
                numeric_value = float(cleaned_item)
                parsed_values.append(numeric_value)
            except ValueError:
                continue
    return parsed_values

def compute_average(numbers):
    if not numbers:
        return 0.0
    total_sum = sum(numbers)
    count = len(numbers)
    return total_sum / count

def process_weight_data(csv_data):
    valid_weights = parse_weights_from_csv(csv_data)
    average_value = compute_average(valid_weights)
    return average_value

if __name__ == '__main__':
    sample_csv_content = "id,weight,status\n1,70.5,ok\n2,abc,error\n3,65.2,ok\n4,,skip\n5,80.1,ok"
    result = process_weight_data(sample_csv_content)
    print(result)