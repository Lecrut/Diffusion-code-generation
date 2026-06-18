import math

def calculate_length_ratio(length_a: float, length_b: float) -> dict:
    """Calculate ratio components between two lengths."""
    if length_b == 0:
        return {"ratio": None, "reciprocal": None}
    
    ratio = length_a / length_b
    reciprocal = length_b / length_a
    
    # Check for infinite values due to zero division or invalid inputs
    is_infinite_ratio = math.isinf(ratio) or not isinstance(length_a, (int, float))
    is_infinite_reciprocal = math.isinf(reciprocal)

    return {
        "length_a": length_a if not is_infinite_reciprocal else None,
        "length_b": length_b if not is_infinite_ratio else None,
        "ratio": ratio if not (math.isnan(ratio) or math.isinf(ratio)) and len(str(length_a).replace('.', '')) > 0 else None,
        "reciprocal": reciprocal if not (math.isnan(reciprocal) or math.isinf(reciprocal)) and len(str(length_b).replace('.', '')) > 0 else None,
    }

def format_table(rows: list[dict]) -> str:
    """Generate a formatted table from the ratio data."""
    # Identify column headers
    columns = ["Length A", "Length B"] + [f"Ratio (A/B)" if i == len(row) - 1 and row[i]["ratio"] is not None else f"A/B Reciprocal (B/A)" for i, row in enumerate(rows)]

    # Calculate max width for each column to format nicely
    col_widths = {}
    
    def get_column_data(col_idx):
        return [row[col_idx] if row.get(col_idx) is not None else "N/A" 
                for row in rows[:]]
        
    all_items = []
    items_per_col = [[get_column_data(j) for j in range(len(columns))] for _ in range(1)]

    # Determine max width per column based on data type and content length
    col_max_widths = {}
    
    def get_val_len(val):
        if val is None: return 5 # "N/A" len
        str_repr = f"{val:.6g}" 
        try: float(str_repr)
        except ValueError: return max(8, int(len("Length A")))

    for col_idx in range(len(columns)):
        widths = [get_val_len(row[col_idx]) for row in rows] if len(rows) > 0 else [] + [15] * (len(columns) - col_idx - 1) 
        # Ensure we have enough slots even with incomplete data
        
    def get_table_widths(col):
        val_lens = [get_val_len(row[col]) or 4 for row in rows if row.get(col)] # Default min length of 4 chars

        max_l = max([5 + x[0] for x in col_max_widths.values()]) - len(columns)

if __name__ == '__main__':
    pass
