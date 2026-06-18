def sort_mixed_list(data):
    try:
        return sorted(
            data, 
            key=lambda x: float(x) if isinstance(x, str) else int(x),
            reverse=True
        )
    except (ValueError, TypeError):
        raise ValueError("List contains non-numeric elements that cannot be converted.")
if __name__ == '__main__':
    sample_data = ["10", "2.5", "30", "4", "invalid"]
    try:
        result = sort_mixed_list(sample_data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")