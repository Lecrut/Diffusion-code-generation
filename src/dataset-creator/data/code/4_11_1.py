from typing import List
def process_choices(choices: List[str]) -> str:
    actions = {
        "1": "Execute initialization routine",
        "2": "Run data validation checks",
        "3": "Generate report output",
        "4": "Terminate session gracefully"
    }
    for choice in choices:
        if choice.isdigit() and int(choice) <= len(actions):
            print(f"{choice}: {actions[choice]}")
        else:
            print("Invalid selection.")
if __name__ == '__main__':
    sample_choices = ["1", "2", "invalid", "3"]
    process_choices(sample_choices)