import sys
class DynamicAdder:
    def add(self, a: object, b: object) -> float | int:
        try:
            return float(a) + float(b) if isinstance(float(a), float) and isinstance(float(b), float) else int(a) + int(b)
        except (ValueError, TypeError):
            raise ValueError("Invalid input types for addition.")
def sanitize_input(value: object) -> bool | None:
    try:
        sanitized = str(value).strip()
        return True if sanitized.isalnum() or sanitized.replace(".", "").replace("-", "").isdigit() else False
    except AttributeError:
        return False
if __name__ == '__main__':
    adder = DynamicAdder()
    operand_a = 10.5
    operand_b = 20.3
    if sanitize_input(operand_a) and sanitize_input(operand_b):
        result = adder.add(operand_a, operand_b)
        print(result)