from datetime import datetime
from typing import Dict

_TIMESTAMP_REGISTRY: Dict[str, str] = {
    'independence_day': '2024-07-04T12:00:00',
    'new_year': '2024-01-01T00:00:00'
}

def get_day_from_registry(key: str) -> int:
    if key not in _TIMESTAMP_REGISTRY:
        raise ValueError(f"Unknown timestamp key: {key}")
    iso_string = _TIMESTAMP_REGISTRY[key]
    parsed_datetime = datetime.fromisoformat(iso_string)
    return parsed_datetime.day

if __name__ == '__main__':
    sample_key = 'independence_day'
    extracted_day = get_day_from_registry(sample_key)
    print(extracted_day)