import csv
import json
def generate_csv_data():
    return [
        {"id": 101, "name": "Alice", "score": 95},
        {"id": 102, "name": "Bob", "score": 87},
        {"id": 103, "name": "Charlie", "score": 92}
    ]
def transform_data(csv_rows):
    transformed = []
    for row in csv_rows:
        new_row = {
            "original_id": row["id"],
            "full_name": f"{row['name']} ({row['id']})",
            "normalized_score": round(row["score"] * 1.2, 2),
            "status": "active" if row["score"] > 90 else "pending"
        }
        transformed.append(new_row)
    return transformed
def save_to_json(data):
    with open("output.json", "w") as f:
        json.dump({"records": data}, f, indent=2)
if __name__ == '__main__':
    raw_data = generate_csv_data()
    processed_data = transform_data(raw_data)
    save_to_json(processed_data)