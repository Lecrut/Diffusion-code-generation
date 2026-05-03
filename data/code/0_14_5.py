def convert_length(length: float, unit: str) -> float:
    conversions = {
        "meters": length,
        "feet": length * 3.28084,
        "kilometers": length * 1000.0
    }
    if unit in conversions:
        return conversions[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    print(convert_length(10, "meters"))
    print(convert_length(10, "feet"))
    print(convert_length(10, "kilometers"))
    try:
        convert_length(10, "miles")
    except ValueError as e:
        print(e)