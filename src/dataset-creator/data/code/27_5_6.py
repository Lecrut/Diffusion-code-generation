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
        if field not in record or record[field] == "":
            return False
    try:
        quantity = int(record['quantity'])
        if quantity < 0:
            return False
    except (ValueError, TypeError):
        return False
    return True
def process_fruits(data):
    logger.info("Starting fruit record processing")
    valid_records = []
    for idx, record in enumerate(data.get('records', [])):
        if not is_valid_record(record):
            logger.warning(f"Skipping invalid record at index {idx}")
            continue
        logger.debug(f"Validating record type: {record['type']}")
        valid_records.append(record)
    grouped = defaultdict(list)
    for rec in valid_records:
        fruit_type = str(rec.get('type', 'unknown'))
        grouped[fruit_type].append({
            "name": rec.get("name", ""), 
            "quantity": int(rec["quantity"]), 
            "price": float(rec.get("price", 0.0)) if isinstance(rec.get("price"), (int, float)) else 0.0
        })
    logger.info(f"Successfully grouped {len(grouped)} fruit types")
    return dict(grouped)
if __name__ == '__main__':
    sample_data = {
        "records": [
            {"type": "apple", "quantity": 10, "price": 0.5},
            {"type": "", "quantity": 5, "price": 0.3},
            None,
            {"type": "banana", "quantity": -2, "price": 0.4},
            {"name": "orange"},
        ]
    }
    try:
        result = process_fruits(sample_data)
        logger.info("Processing completed successfully")
        print(json.dumps(result))
    except Exception as e:
        logger.error(f"Unexpected error occurred during processing: {e}")