import argparse
import json
import os
def create_store_data(data):
    with open("store_data.json", "w") as f:
        json.dump(data, f, indent=4)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A CLI to save sample store data to a JSON file.")
    parser.add_argument("--items", type=str, default='{"products": [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Mouse"}], "inventory": {"Laptop": 5, "Mouse": 10}}', help="JSON string containing the store data.")
    parser.add_argument("--filename", type=str, default="store_data.json", help="The name of the output JSON file.")
    args = parser.parse_args()
    try:
        store_data = json.loads(args.items)
        create_store_data(store_data)
        print(f"Successfully saved store data to {args.filename}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON provided for --items argument.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")