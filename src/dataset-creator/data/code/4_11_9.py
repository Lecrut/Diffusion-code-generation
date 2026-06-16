def process_choices(choices):
    actions = {
        "1": "Execute startup sequence",
        "2": "Run diagnostic checks",
        "3": "Generate report data",
        "4": "Exit system gracefully"
    }
    results = []
    for choice in choices:
        if choice not in actions:
            continue
        action_name = actions[choice]
        if 1 <= int(choice) <= len(actions):
            result_message = f"Performing {action_name}..."
            results.append(result_message)
    return "\n".join(results)
if __name__ == '__main__':
    sample_choices = ["2", "3", "invalid"]
    output = process_choices(sample_choices)
    print(output)