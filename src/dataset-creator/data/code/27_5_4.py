import json
import logging
from collections import defaultdict
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def validate_fruit_record(record):
    if not isinstance(record, dict):
        return False
    required_fields = ['type', 'quantity']
    for field in required_fields:
        if field not in record or record[field] is None:
            logger.warning(f"Invalid record missing required field '{field}'")
            return False
    try:
        quantity = float(record['quantity'])
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
    except (ValueError, TypeError):
        logger.error(f"Invalid quantity value in record {record}")
        return False
    return True
def process_fruits(json_input):
    valid_entries = []
    invalid_count = 0
    if not isinstance(json_input, list):
        json_input = [json_input]
    for i, record in enumerate(json_input):
        logger.info(f"Processing record {i + 1}")
        if validate_fruit_record(record):
            valid_entries.append(record)
            logger.debug("Record validated successfully")
        else:
            invalid_count += 1
            logger.warning(f"Skipping invalid record at index {i}")
    grouped = defaultdict(list)
    for entry in valid_entries:
        fruit_type = str(entry['type']).strip().lower()
        if not fruit_type or 'fruit' not in fruit_type and type != 'Fruit':
             continue 
        grouped[fruit_type].append(entry)
    return dict(grouped), invalid_count
if __name__ == '__main__':
    sample_data = [
        {"type": "Apple", "quantity": 10},
        {"type": "Banana"},
        {"type": "Orange", "quantity": -5},
        {"type": "Mango", "quantity": "twenty"}
    ]
    logger.info("Starting fruit data processing")
    grouped_fruits, invalid_count = process_fruits(sample_data)
    for fruit_type, entries in grouped_fruits.items():
        logger.info(f"Group '{fruit_type}': {len(entries)} items processed")