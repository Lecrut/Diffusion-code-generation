import json
def detect_uniform_values(data):
    if not data:
        return {"status": "empty", "message": "Input dataset is empty."}
    uniform_rows = []
    for row in data:
        if isinstance(row, list) and len(row) > 0:
            try:
                first_val = str(row[0])
                all_same = all(str(x) == first_val for x in row)
                if all_same:
                    uniform_rows.append({"row_index": len(uniform_rows), "values": row, "is_uniform": True})
            except Exception as e:
                continue
        else:
            continue
    return {"status": "success", "uniform_count": len(uniform_rows), "details": uniform_rows}
if __name__ == '__main__':
    sample_data = [
        ["a", "b"],
        [],
        ["5", "5", "5"],
        None,
        ["x", "y", "z"]
    ]
    result = detect_uniform_values(sample_data)
    print(json.dumps(result, indent=2))