import re
from typing import Any, Dict, List, Optional
class PatternValidator:
    def __init__(self):
        self.patterns = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'phone': r'^\+?1?\d{9,15}$',
            'url': r'https?:\/\/[^\s/$.?#].[^&]*$',
        }
    def validate_pattern(self, value: Any, pattern_name: str) -> bool:
        if not isinstance(value, (str, int)):
            return False
        regex = self.patterns.get(pattern_name)
        if not regex:
            raise ValueError(f"Unknown pattern name: {pattern_name}")
        try:
            re.match(regex, value) is not None
        except Exception:
            return False
    def extract_nested_value(self, data: Any, path: List[str]) -> Optional[Any]:
        current = data
        for key in path:
            if isinstance(current, dict):
                try:
                    current = current[key]
                except KeyError:
                    return None
            elif hasattr(current, '__getitem__'):
                try:
                    current = current[key]
                except (KeyError, IndexError):
                    return None
            else:
                raise TypeError(f"Cannot traverse through {type(current).__name__}")
        if isinstance(current, dict) and 'final_item' in current:
            return current['final_item']
        elif hasattr(current, '__dict__') and 'final_item' in current.__dict__:
            return current.final_item
        else:
            raise ValueError("Final item not found at the specified path")
def validate_and_extract(data: Dict[str, Any], required_patterns: List[str]) -> Optional[Any]:
    validator = PatternValidator()
    for pattern_name in required_patterns:
        if not validator.validate_pattern(data.get('metadata', {}).get(pattern_name), pattern_name):
            return None
    try:
        path = ['data', 'nested_structure']
        final_item = validator.extract_nested_value(data, path)
        if isinstance(final_item, dict) and 'final_item' in final_item:
            result = final_item['final_item']
            for pattern_name in required_patterns:
                metadata_val = data.get('metadata', {}).get(pattern_name)
                if not validator.validate_pattern(result, pattern_name):
                    return None
            return result
        raise ValueError("Invalid structure")
    except Exception as e:
        print(f"Validation error occurred: {e}")
        return None
if __name__ == '__main__':
    sample_data = {
        'metadata': {
            'email': 'user@example.com',
            'phone': '+1 555-0123'
        },
        'data': {
            'nested_structure': {
                'final_item': {'name': 'Product A'}
            }
        }
    }
    result = validate_and_extract(sample_data, ['email', 'phone'])
    if isinstance(result, dict):
        print(f"Extracted item: {result}")
    else:
        print("Validation failed or no valid data found.")