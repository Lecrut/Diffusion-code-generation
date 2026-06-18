import json
def detect_uniform_values(data):
    if not data:
        return {"status": "empty", "message": "Input dataset is empty"}
    uniform_rows = []
    for row in data:
        try:
            if isinstance(row, list) and len(row) > 0:
                first_val = row[0]
                all_same = True
                if all(item == first_val for item in row):
                    uniform_rows.append(row)
            else:
                return {"status": "error", "message": f"Invalid row format encountered at index {data.index(row)}"}
        except Exception as e:
            return {"status": "error", "message": str(e), "row_index": data.index(row)}
    if not uniform_rows:
        return {"status": "no_uniforms_found", "uniform_count": 0}
    return {
        "status": "success", 
        "uniform_count": len(uniform_rows), 
        "data": uniform_rows,
        "sample_row": uniform_rows[0] if uniform_rows else None
    }
if __name__ == '__main__':
    sample_data = [
        ["1", "2"],
        ["5", "5"],
        [],
        [[3], [3]],
        [["a", "b"]],
        [{"x": 1}, {"y": 2}]                                                                       
    ]
    result = detect_uniform_values(sample_data)
    print(json.dumps(result, indent=4))