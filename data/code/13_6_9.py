import collections

def get_column_values(data, col_name):
    if not isinstance(data, list):
        raise TypeError("Expected a list of dictionaries.")
    if not isinstance(col_name, str):
        raise TypeError("Column name must be a string.")
    
    result = []
    for item in data:
        if not isinstance(item, dict):
            raise TypeError("Each item must be a dictionary.")
        if col_name not in item:
            raise KeyError(f"Column '{col_name}' not found in {item}")
        result.append(item[col_name])
    return result

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "score": 90},
        {"id": 2, "name": "Bob", "score": 85},
        {"id": 3, "name": "Charlie", "score": 78}
    ]
    
    names = get_column_values(sample_data, "name")
    scores = get_column_values(sample_data, "score")
    
    print(f"Names: {names}")
    print(f"Scores: {scores}")