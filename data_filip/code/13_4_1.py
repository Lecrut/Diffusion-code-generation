import re

def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)

if __name__ == '__main__':
    sample_data = ['user_id', 'first_name', 'total_amount', 'is_active', 'created_at']
    for data in sample_data:
        print(snake_to_camel(data))