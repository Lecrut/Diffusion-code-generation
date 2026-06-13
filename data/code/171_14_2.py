import argparse
import json
import os
def create_store_data(data):
    with open("store_data.json", "w") as f:
        json.dump(data, f, indent=4)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CLI to save hardcoded store data to a JSON file.")
    parser.add_argument("--store-name", type=str, default="SampleStore", help="Name of the store.")
    parser.add_argument("--items", type=str, default='[{"id": 1, "name": "Laptop", "price": 1200.50}, {"id": 2, "name": "Mouse", "price": 25.99}]', help="JSON string of store items.")
    parser.add_argument("--filename", type=str, default="store_data.json", help="Output filename for the JSON data.")
    args = parser.parse_args()
    try:
        store_data = {
            "store_name": args.store_name,
            "items": json.loads(args.items)
        }
        create_store_data(store_data)
        print(f"Successfully saved store data for '{args.store_name}' to {args.filename}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format provided for items.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")