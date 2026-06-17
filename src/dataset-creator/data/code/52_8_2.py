import re
from dataclasses import dataclass
@dataclass
class InputValidator:
    def validate_dict(self, obj):
        if not isinstance(obj, dict) and not hasattr(obj, '__dict__'):
            raise TypeError("Input must be a dictionary or object instance")
        required_keys = ['name', 'value']
        for key in required_keys:
            if key not in obj.__dict__:
                raise ValueError(f"Missing required key '{key}' in input structure")
    def validate_list(self, obj):
        if not isinstance(obj, list) or len(obj) == 0:
            raise TypeError("Input must be a non-empty list")
    def extract_final_item(self, data_structure):
        self.validate_dict(data_structure)
        name = data_structure['name']
        value = data_structure.get('value')
        if isinstance(value, dict):
            return self.extract_final_item(value)
        elif hasattr(value, '__dict__'):
            obj_type = type(value).__name__.lower()
            pattern1 = r'^([a-z]+)-(\d+)$'
            match = re.match(pattern1, name.lower())
            if not match:
                raise ValueError(f"Invalid format for '{obj_type}' data")
        return value
if __name__ == '__main__':
    sample_data_1 = {
        'name': 'user_profile',
        'value': {'id': 42, 'type': 'active'}
    }
    sample_data_2 = [
        {'name': 'config_v1', 'value': {'status': True}},
        {'name': 'settings_beta', 'value': False}
    ]
    validator = InputValidator()
    try:
        result = validator.extract_final_item(sample_data_1)
        print(f"Result from dict structure: {result}")
        if isinstance(result, list):
            for item in result:
                final_result = validator.extract_final_item(item)
                print(f"Final extracted value: {final_result}")
    except Exception as e:
        print(f"Validation Error: {e}")