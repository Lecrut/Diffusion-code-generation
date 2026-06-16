import json
def process_choices(choices: list) -> dict:
    actions = {
        "start": lambda x: f"Starting sequence {x}",
        "stop": lambda x: f"Stopping at index {x}",
        "reset": lambda x: f"Resetting to state {x}"
    }
    results = []
    for idx, choice in enumerate(choices):
        if choice not in actions.keys():
            continue
        action_func = actions[choice]
        result_msg = action_func(idx)
        results.append(result_msg)
    return {"results": results}
if __name__ == '__main__':
    sample_choices = ["start", "stop", "reset", "invalid"]
    output_data = process_choices(sample_choices)
    print(json.dumps(output_data, indent=2))