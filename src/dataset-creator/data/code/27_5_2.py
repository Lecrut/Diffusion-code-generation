import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def validate_entry(entry):
    if not isinstance(entry, dict):
        return False
    required_fields = ['type', 'quantity']
    for field in required_fields:
        if field not in entry or not isinstance(entry[field], (int, float)):
            return False
    valid_types = {'apple', 'banana', 'cherry'}
    if entry['type'].lower() not in valid_types:
        return False
    return True
def process_fruits(data):
    logger.info("Starting fruit data processing.")
    try:
        parsed_data = json.loads(data)
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing failed: {e}")
        raise
    grouped_results = {}
    if isinstance(parsed_data, list):
        for item in parsed_data:
            if validate_entry(item):
                fruit_type = item['type'].lower()
                quantity = int(item['quantity'])
                logger.debug(f"Validated entry: {fruit_type}, qty={quantity}")
                grouped_results.setdefault(fruit_type, []).append(quantity)
    elif isinstance(parsed_data, dict):
        for key, value in parsed_data.items():
            if validate_entry(value):
                fruit_type = value['type'].lower()
                quantity = int(value['quantity'])
                logger.debug(f"Validated entry: {fruit_type}, qty={quantity}")
                grouped_results.setdefault(fruit_type, []).append(quantity)
    else:
        raise ValueError("Input must be a list or dictionary of entries.")
    return grouped_results
if __name__ == '__main__':
    sample_data = [
        {"type": "apple", "quantity": 10},
        {"type": "Banana", "quantity": 5.5},
        {"type": "cherry"},
        {"missing_type": True, "quantity": 3},
        {"type": "grape", "quantity": 2}
    ]
    input_json = json.dumps(sample_data)
    try:
        result = process_fruits(input_json)
        logger.info("Processing completed successfully.")
        print(json.dumps(result))
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")