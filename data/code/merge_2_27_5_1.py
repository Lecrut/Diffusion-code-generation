import json
import logging
from collections import defaultdict
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def is_valid_entry(entry):
    if not isinstance(entry, dict):
        return False
    required_fields = ['type', 'quantity']
    for field in required_fields:
        if field not in entry or entry[field] == '' or entry[field] is None:
            logger.warning(f"Invalid entry missing or empty {field}: {entry}")
            return False
    try:
        int(entry['quantity'])
    except ValueError:
        logger.error(f"Entry has invalid quantity type for key 'type': {entry.get('type')}")
        return False
    if not isinstance(entry['type'], str):
        logger.warning("Invalid entry with non-string type field.")
        return False
    return True
def process_fruits(data):
    valid_entries = []
    invalid_count = 0
    for idx, item in enumerate(data.get('records', [])):
        if is_valid_entry(item):
            valid_entries.append(item)
        else:
            logger.warning(f"Skipping record at index {idx} due to validation failure.")
            invalid_count += 1
    return {'valid': valid_entries, 'invalid_skipped': invalid_count}
def group_by_type(entries):
    grouped = defaultdict(list)
    for entry in entries:
        fruit_type = str(entry['type']).lower()
        grouped[fruit_type].append({
            'quantity': int(entry['quantity']),
            'original_entry': entry
        })
    result_dict = {}
    for key, value_list in sorted(grouped.items()):
        total_quantity = sum(item['quantity'] for item in value_list)
        count = len(value_list)
        result_dict[key] = {'total_count': count, 'sum_of_quantities': total_quantity}
    return dict(result_dict)
if __name__ == '__main__':
    sample_data = {
        "records": [
            {"type": "apple", "quantity": 10},
            {"type": "banana", "quantity": ""},
            {"type": "orange"},
            {"type": "grape", "quantity": -5},
            {"type": "mango", "quantity": "twenty"},
        ]
    }
    logger.info("Starting fruit record processing.")
    try:
        processed = process_fruits(sample_data)
        grouped_results = group_by_type(processed['valid'])
        logger.info(f"Processing complete. Valid records found: {len(processed['valid'])}. Invalid skipped: {processed['invalid_skipped']}.")
        for fruit, stats in grouped_results.items():
            logger.info(f"Fruit type '{fruit}': Count={stats['total_count']}, Total Quantity={stats['sum_of_quantities']}")
    except Exception as e:
        logger.exception("An unexpected error occurred during processing.")