class FixedWidthParser:
    def __init__(self, field_start_indices: list[int], field_end_indices: list[int]):
        self.field_start_indices = field_start_indices
        self.field_end_indices = field_end_indices

    def parse(self, data_string: str) -> dict[str, str]:
        fields = {}
        for start, end in zip(self.field_start_indices, self.field_end_indices):
            if start < end:
                fields[f"field_{start}_{end}"] = data_string[start:end].strip()
        return fields

if __name__ == '__main__':
    parser = FixedWidthParser([0, 5, 10], [4, 9, 14])
    sample_data = "HelloWorldPython"
    parsed_data = parser.parse(sample_data)
    print(f"Input String: {sample_data}")
    print("Parsed Data:")
    for key, value in parsed_data.items():
        print(f"{key}: {value}")