def convert_length(length: float, target_unit: str) -> float:
    units = {
        "meters": 1.0,
        "feet": 3.28084,
        "kilometers": 0.001
    }
    if target_unit not in units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    return length / units[target_unit]

if __name__ == "__main__":
    print(convert_length(100, "feet"))
    print(convert_length(5000, "kilometers"))
    print(convert_length(1, "meters"))