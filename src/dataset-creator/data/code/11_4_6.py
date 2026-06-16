import json
def detect_uniform_values(data):
    if not data:
        return {"status": "empty", "message": "Input dataset is empty"}
    uniform_rows = []
    for row in data:
        try:
            if isinstance(row, list) and len(row) > 0:
                first_value = row[0]
                all_same = True
                for item in row:
                    if item != first_value:
                        all_same = False
                        break
                if all_same and len(row) > 0:
                    uniform_rows.append({"row_index": data.index(row), "values": row})
            else:
                if isinstance(row, (list, tuple)) and len(row) == 1:
                    uniform_rows.append({"row_index": data.index(row), "values": row})
        except Exception as e:
            continue
    return {"status": "success", "uniform_count": len(uniform_rows), "data": uniform_rows}
if __name__ == '__main__':
    sample_data = [
        ["1", "2"],
        ["5", "5"],
        [],
        [[3], [4, 4]],
        None,
        {"a": "b"}
    ]
    result = detect_uniform_values(sample_data)
    print(json.dumps(result, indent=2))