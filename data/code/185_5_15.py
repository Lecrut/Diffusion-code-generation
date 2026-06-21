def validate_indices(indices):
    if not all(isinstance(i, int) and i >= 0 for i in indices):
        raise ValueError("Indices must be non-negative integers")
    if len(set(indices)) != len(indices):
        raise ValueError("Indices must be unique")

def parse_fixed_width_string(data_string: str, start_indices: list[int], end_indices: list[int]) -> dict:
    validate_indices(start_indices)
    validate_indices(end_indices)

    if not all(s < e for s, e in zip(start_indices, end_indices)):
        raise ValueError("Start index must be less than end index for each field")

    if len(start_indices) != len(end_indices):
        raise ValueError("Number of start and end indices must be the same")

    fields = {}
    for i, (start, end) in enumerate(zip(start_indices, end_indices)):
        fields[f'field{i+1}'] = data_string[start:end].strip()

    return fields

if __name__ == '__main__':
    sample_data = "JohnDoe30NewYork"
    start_indices = [0, 5, 8]
    end_indices = [5, 8, len(sample_data)]
    parsed_data = parse_fixed_width_string(sample_data, start_indices, end_indices)
    print(f"Input String: {sample_data}")
    print("Parsed Data:")
    for key, value in parsed_data.items():
        print(f"{key}: {value}")