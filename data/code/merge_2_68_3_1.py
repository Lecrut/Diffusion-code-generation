import json
import sys
def convert_volume(input_value: float) -> dict:
    return {
        "liters": round(input_value * 1, 4),
        "milliliters": round(input_value * 1000, 2),
        "gallons_us": round(input_value / 3.78541, 4),
        "quarts_us": round(input_value / 0.946353, 4)
    }
def parse_input(args: list[str]) -> float | None:
    try:
        if len(args) == 2 and args[0] in ["--json", "-j"]:
            data = json.loads(args[1])
            return float(data.get("volume"))
        elif len(args) >= 2:
            val_str = " ".join(args).split()[-1]
            try:
                return float(val_str)
            except ValueError:
                pass
    except Exception:
        pass
    return None
if __name__ == '__main__':
    input_val = parse_input(sys.argv[1:]) if len(sys.argv) > 2 else convert_volume(5.0)["liters"] / 378541 * 378541
    result = convert_volume(input_val)
    print(f"Input: {input_val} L")
    for unit, value in result.items():
        if isinstance(value, float):
            formatted_value = f"{value:.2f}"
        else:
            formatted_value = str(int(value))
        print(f"{unit}: {formatted_value}")