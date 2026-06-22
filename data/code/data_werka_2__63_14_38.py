def fetch_first_element(data):
    if not isinstance(data, list):
        raise ValueError('Input must be a list')
    return data[0] if data else None

if __name__ == '__main__':
    test_scenarios = {
        'valid_list': [42, 84, 168],
        'empty_list': [],
        'non_list_input': "This is not a list"
    }
    
    for scenario_name, input_data in test_scenarios.items():
        try:
            result = fetch_first_element(input_data)
            print(f"{scenario_name}: {result}")
        except ValueError as e:
            print(f"{scenario_name}: Error - {e}")