def convert_length(length: float, target_unit: str) -> float:
    if target_unit == "meters":
        return length
    elif target_unit == "feet":
        return length * 3.28084
    elif target_unit == "kilometers":
        return length * 0.001
    else:
        raise ValueError(f"Unsupported unit: {target_unit}")

if __name__ == "__main__":
    result = convert_length(100, "feet")
    print(result)