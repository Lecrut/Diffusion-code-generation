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
    for idx, entry in enumerate(data):
        logger.debug(f"Processing record {idx}")
        if is_valid_entry(entry):
            fruit_type = entry['type']
            quantity = int(entry['quantity'])
            valid_entries.append({'type': fruit_type, 'quantity': quantity})
            current_count = sum(e['quantity'] for e in valid_entries if e['type'] == fruit_type)
            logger.info(f"Added {fruit_type} with total count: {current_count}")
        else:
            logger.warning(f"Ignoring invalid record at index {idx}: {entry}")
    grouped = {}
    for entry in valid_entries:
        t = entry['type']
        if t not in grouped:
            grouped[t] = 0
        grouped[t] += entry['quantity']
    logger.info("Processing completed successfully")
    return grouped
if __name__ == '__main__':
    sample_data = [
        {"type": "apple", "quantity": "5"},
        {"type": "banana", "quantity": ""},
        {"type": "orange", "quantity": 3.0},
        {"type": "grape", "quantity": "12"}
    ]
    result = process_fruits(sample_data)
    logger.info(f"Final grouped data: {result}")