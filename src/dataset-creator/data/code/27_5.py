import json
import logging
from collections import defaultdict
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def is_valid_record(record):
    if not isinstance(record, dict):
        return False
    required_fields = ['type', 'quantity']
    for field in required_fields:
        if field not in record or not isinstance(record[field], (int, float)):
            return False
    return True
def process_fruits(json_input):
    logger.info("Starting fruit processing")
    valid_entries = []
    try:
        data = json.loads(json_input)
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing failed: {e}")
        raise
    if not isinstance(data, list):
        logger.warning("Input is not a JSON array")
        return []
    for index, record in enumerate(data):
        logger.info(f"Processing record at index {index}: {record.get('type', 'unknown')}")
        if is_valid_record(record):
            valid_entries.append(record)
            logger.debug(f"Record added to valid list: type={record['type']}, quantity={record['quantity']}")
        else:
            logger.warning(f"Skipping invalid record at index {index}: missing or incorrect fields")
    grouped = defaultdict(list)
    for entry in valid_entries:
        fruit_type = str(entry.get('type', 'unknown'))
        grouped[fruit_type].append({
            "quantity": int(entry['quantity']),
            "name": entry.get('name', '')
        })
    logger.info(f"Processing complete. Found {len(grouped)} unique types.")
    return dict(grouped)
if __name__ == '__main__':
    sample_data = [
        {"type": "apple", "quantity": 5, "name": "Red Apple"},
        {"type": "banana", "quantity": 3},
        {"type": "orange", "quantity": -2},
        {"type": "grape", "quantity": 10, "name": "Green Grape"},
        {"missing_field": True},
        {"type": "pear"}
    ]
    json_str = json.dumps(sample_data)
    try:
        result = process_fruits(json_str)
        logger.info("Output generation started")
        for fruit_type, entries in sorted(result.items()):
            total_qty = sum(e['quantity'] for e in entries)
            names = [e['name'] if 'name' in e else '' for e in entries]
            output_line = f"{fruit_type}: {len(entries)} items (Total Qty: {total_qty}) - Names: {'; '.join(names)}"
            logger.info(output_line)
    except Exception as e:
        logger.critical(f"Unexpected error during processing: {e}")