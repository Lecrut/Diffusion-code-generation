import json
def generate_csv_data():
    return [
        {"id": 101, "name": "Alice", "score": 95},
        {"id": 102, "name": "Bob", "score": 87},
        {"id": 103, "name": "Charlie", "score": 92}
    ]
def transform_to_json(csv_data):
    return {
        "metadata": {
            "source": "internal_generation",
            "version": "1.0"
        },
        "records": csv_data,
        "statistics": {
            "total_records": len(csv_data),
            "avg_score": sum(record["score"] for record in csv_data) / len(csv_data) if csv_data else 0
        }
    }
def main():
    raw_csv = generate_csv_data()
    final_json = transform_to_json(raw_csv)
    print(json.dumps(final_json, indent=2))
if __name__ == '__main__':
    main()