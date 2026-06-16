import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def is_valid_entry(entry):
    if not isinstance(entry, dict):
        return False
    required_fields = ['type', 'quantity']
    for field in required_fields:
        if field not in entry or entry[field] == "":
            return False
    try:
        int(entry['quantity'])
    except ValueError:
        return False
    return True
def process_fruits(data):
    logger.info("Starting fruit data processing")
    valid_entries = []
    if not isinstance(data, list):
        logger.error("Input must be a JSON array of records")
        return {}
    for index, entry in enumerate(data):
        logger.debug(f"Processing record {index}")
        if is_valid_entry(entry):
            fruit_type = entry['type']
            quantity = int(entry['quantity'])
            valid_entries.append({'type': fruit_type, 'quantity': quantity})
            current_count = sum(e['quantity'] for e in valid_entries if e['type'] == fruit_type)
            logger.info(f"Added {fruit_type} with total count: {current_count}")
        else:
            logger.warning(f"Ignoring invalid record at index {index}: {entry}")
    grouped_data = {}
    for entry in valid_entries:
        if entry['type'] not in grouped_data:
            grouped_data[entry['type']] = 0
        grouped_data[entry['type']] += entry['quantity']
    logger.info("Processing completed successfully")
    return grouped_data
if __name__ == '__main__':
    sample_input = [
        {"type": "apple", "quantity": "5"},
        {"type": "banana", "quantity": ""},
        {"type": "orange", "quantity": 3.0},
        {"type": "grape", "quantity": "10"}
    ]
    try:
        json_input = json.dumps(sample_input)
        parsed_data = json.loads(json_input)
        result = process_fruits(parsed_data)
        logger.info(f"Final grouped data: {result}")
    except Exception as e:
        logger.error(f"Error during processing: {e}", exc_info=True)