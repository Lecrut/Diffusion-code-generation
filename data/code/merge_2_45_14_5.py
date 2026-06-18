import re
def sanitize_input(value: str) -> float | int:
    pattern = r'^[-+]?(\d+(\.\d+)?)$'
    if not re.match(pattern, value):
        raise ValueError("Invalid numeric input")
    return float(value)
class DynamicAdder:
    def __init__(self):
        self._last_error = None
    def add(self, a_str: str | int | float, b_str: str | int | float) -> float:
        try:
            if isinstance(a_str, (int, float)):
                a_val = sanitize_input(str(a_str))
            else:
                a_val = sanitize_input(a_str)
            if isinstance(b_str, (int, float)):
                b_val = sanitize_input(str(b_str))
            else:
                b_val = sanitize_input(b_str)
            return a_val + b_val
        except Exception as e:
            self._last_error = str(e)
            raise
if __name__ == '__main__':
    adder = DynamicAdder()
    result = adder.add("12.5", "43")
    print(result)