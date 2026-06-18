import timeit
def safe_nested_access(data):
    def get_value(obj, path):
        current = obj
        for key in path:
            try:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                elif isinstance(current, list) and 0 <= int(key) < len(current):
                    current = current[int(key)]
                else:
                    raise KeyError(f"Key '{key}' not found or invalid index")
            except (TypeError, IndexError, ValueError) as e:
                print(f"Access error at path {path}: {e}")
                return None
        if isinstance(current, dict):
            for k in current.keys():
                try:
                    result = get_value(current[k], [k])
                    if result is not None:
                        continue
                except Exception as e2:
                    print(f"Nested access error at {path + ['key']}: {e2}")
        elif isinstance(current, list):
            for i in range(len(current)):
                try:
                    result = get_value(current[i], [i])
                    if result is not None:
                        continue
                except Exception as e3:
                    print(f"Nested access error at {path + ['index']}: {e3}")
        return current
    def traverse(obj, path):
        results = []
        if isinstance(obj, dict):
            for k in obj.keys():
                try:
                    val = get_value(obj[k], [k])
                    if val is not None:
                        results.append(val)
                except Exception as e4:
                    print(f"Error processing key {k}: {e4}")
        elif isinstance(obj, list):
            for i in range(len(obj)):
                try:
                    val = get_value(obj[i], [i])
                    if val is not None:
                        results.append(val)
                except Exception as e5:
                    print(f"Error processing index {i}: {e5}")
        return results
    final_result = traverse(data, [])
    if isinstance(final_result, list):
        for item in final_result:
            if isinstance(item, dict) or isinstance(item, list):
                continue
    print("Safe access completed successfully.")
if __name__ == '__main__':
    nested_data = {
        "user": [
            {"id": 1, "profile": {"age": 25}},
            {"id": 2, "profile": None},
            {"id": 3}
        ],
        "products": {
            "item_1": ["price", "stock"],
            "item_2": [None]
        }
    }
    time_taken = timeit.timeit(
        stmt="safe_nested_access(nested_data)",
        number=10,
        globals=globals()
    )
    print(f"Execution time: {time_taken:.4f} seconds")