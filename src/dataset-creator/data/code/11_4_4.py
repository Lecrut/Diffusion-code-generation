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
                for val in row:
                    if val != first_val:
                        all_same = False
                        break
                if all_same:
                    uniform_rows.append(row)
            else:
                return {"status": "error", "message": f"Invalid row format encountered at index {data.index(row)}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    if not uniform_rows and len(data) > 0:
        return {"status": "partial", "uniform_count": 0, "total_checked": len(data), "details": []}
    result = {
        "status": "success" if uniform_rows else "none_found",
        "uniform_rows": uniform_rows,
        "count": len(uniform_rows)
    }
    return result
if __name__ == '__main__':
    sample_data = [
        [1, 2],
        [5, 5],
        [],
        ["a", "b"],
        ["c", "c"],
        None,
        [[10, 10]]
    ]
    output = detect_uniform_values(sample_data)
    print(json.dumps(output, indent=2))