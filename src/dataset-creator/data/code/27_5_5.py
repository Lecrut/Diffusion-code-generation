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
            fruit_type = str(entry['type']).lower()
            valid_entries.append({
                'type': fruit_type,
                'quantity': int(entry['quantity'])
            })
    grouped_data = {}
    for entry in valid_entries:
        f_type = entry['type']
        if f_type not in grouped_data:
            grouped_data[f_type] = {'count': 0, 'total_quantity': 0}
        grouped_data[f_type]['count'] += 1
        grouped_data[f_type]['total_quantity'] += entry['quantity']
    logger.info(f"Processed {len(valid_entries)} valid entries")
    return grouped_data
if __name__ == '__main__':
    sample_input = [
        {"type": "apple", "quantity": 5},
        {"type": "banana", "quantity": ""},
        {"type": "orange"},
        {"type": "grape", "quantity": 10},
        None,
        {"type": "mango", "quantity": -3}
    ]
    result = process_fruits(sample_input)
    logger.info(f"Final grouped data: {result}")