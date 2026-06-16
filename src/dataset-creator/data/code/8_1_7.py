import json
from typing import List, Dict
def process_records(records: List[Dict], conditions: Dict) -> List[Dict]:
    filtered = []
    for record in records:
        try:
            if (conditions.get('status') and record['status'] != 'active') or\
               (conditions.get('min_value') is not None and record['value'] < conditions['min_value']):
                continue
            transformed_record = {
                **record,
                'processed': True,
                'score': round(record['value'] * 1.5 + 10, 2) if conditions.get('transform_score') else record.get('score', 0)
            }
            filtered.append(transformed_record)
        except Exception:
            continue
    return filtered
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'status': 'active', 'value': 50},
        {'id': 2, 'status': 'inactive', 'value': 75},
        {'id': 3, 'status': 'active', 'value': 40}
    ]
    conditions = {
        'status': True,
        'min_value': None,
        'transform_score': False
    }
    result = process_records(sample_data, conditions)
    print(json.dumps(result, indent=2))