import json
from datetime import date, timedelta
def generate_item_list():
    items = []
    base_date = date.today()
    for i in range(10):
        item_id = f"ITEM-{i+1:03d}"
        try:
            quantity = 5 + (i % 4) * 2
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Invalid quantity")
            description = f"{item_id} - {chr(65+i)} Series"
            items.append({
                "id": item_id,
                "quantity": quantity,
                "description": description,
                "created_at": (base_date + timedelta(days=i)).isoformat()
            })
        except ValueError as ve:
            print(f"[ERROR] {ve}")
    return items
if __name__ == '__main__':
    output_data = generate_item_list()
    try:
        with open("item_list.json", "w") as file_handle:
            json.dump(output_data, file_handle, indent=4)
        print(f"[INFO] Successfully generated {len(output_data)} items.")
    except IOError as ie:
        print("[CRITICAL] Failed to write output file:", str(ie))