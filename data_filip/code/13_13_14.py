def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    if not parts:
        return ''
    first, *rest = parts
    return first + ''.join(word.capitalize() for word in rest)

if __name__ == '__main__':
    test_cases = ['user_id', 'total_amount_paid', 'max_retry_count', 'is_active', 'singleword']
    for case in test_cases:
        print(snake_to_camel(case))