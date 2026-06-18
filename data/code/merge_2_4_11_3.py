import json
def process_choices(choices: list) -> dict:
    result = {}
    for idx, choice in enumerate(choices):
        if isinstance(choice, str):
            action_map = {
                'start': lambda r: {'status': 'initialized'},
                'stop': lambda r: {'status': 'terminated', 'reasons': []},
                'restart': lambda r: {'status': 'restarting'},
                'config': lambda r: {'action': 'load_config'}
            }
            if choice in action_map:
                result[idx] = {**result.get(idx, {}), **action_map[choice](result)}
        elif isinstance(choice, int):
            threshold_check = idx > 5
            if not threshold_check and len(result) < 3:
                result[idx] = {'type': 'data', 'value': f"item_{idx}"}
            if choice == 10:
                result[idx] = {**result.get(idx, {}), **{'triggered_alert': True}}
    return result
if __name__ == '__main__':
    sample_choices = ['start', 2, 'config', 'stop', 5, 'restart']
    final_output = process_choices(sample_choices)
    print(json.dumps(final_output, indent=4))