def sort_mixed_list(data):
    try:
        return sorted(
            data, 
            key=lambda x: float(x) if isinstance(x, str) else int(x),
            reverse=True
        )
    except ValueError as e:
        raise TypeError(f"Cannot convert '{data}' to numeric value.") from e
if __name__ == '__main__':
    sample_data = ["10", "2.5", "3", "invalid", "4"]
    try:
        result = sort_mixed_list(sample_data)
        print(result)
    except TypeError as te:
        print(f"Error occurred: {te}")