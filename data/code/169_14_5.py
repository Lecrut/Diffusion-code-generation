import json
import os
DATA_FILE = "item_counts.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)
def add_item(data, item, count):
    if item in data:
        data[item] += count
    else:
        data[item] = count
    save_data(data)
def view_counts(data):
    for item, count in data.items():
        print(f"{item}: {count}")
if __name__ == '__main__':
    data = load_data()
    print("--- Item Count Manager CLI ---")
    print("Commands: add <item> <count>, view, exit")
    sample_commands = [
        ("add", "apples", 10),
        ("add", "bananas", 5),
        ("add", "apples", 3),
        ("view",),
        ("exit",)
    ]
    for cmd, *args in sample_commands:
        if cmd == "add":
            if len(args) == 2:
                item = args[0]
                try:
                    count = int(args[1])
                    add_item(data, item, count)
                    print(f"Added {count} of {item}.")
                except ValueError:
                    print("Invalid count. Please use an integer.")
            else:
                print("Usage: add <item> <count>")
        elif cmd == "view":
            view_counts(data)
        elif cmd == "exit":
            print("Exiting program.")
            break
    print("\n--- Final Counts ---")
    view_counts(data)
    save_data(data)