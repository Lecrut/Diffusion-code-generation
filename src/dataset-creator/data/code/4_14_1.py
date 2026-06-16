import argparse
from typing import Dict, Any, List
def validate_input(data: Dict[str, Any]) -> bool:
    required_keys = ["command", "value"]
    return all(key in data for key in required_keys) and isinstance(data["value"], (int, str))
class CommandProcessor:
    def __init__(self):
        self.commands = {
            "add": lambda v: f"Added value: {v}",
            "subtract": lambda v: f"Subtracted value: -{v}",
            "multiply": lambda v: f"Multiply by factor: {int(v)}",
            "divide": lambda v: None if float(v) == 0 else f"Divide result: /{float(v)}",
        }
    def execute(self, command: str, value: Any) -> str:
        cmd_lower = command.lower()
        handler = self.commands.get(cmd_lower)
        if not handler or validate_input({"command": command, "value": value}):
            return f"Error: Invalid input for '{cmd_lower}'."
        try:
            result = handler(value)
            return result if isinstance(result, str) else f"{handler.__name__} failed validation."
        except Exception as e:
            return f"Execution error in {cmd_lower}: {str(e)}"
def parse_args() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(description="High-performance command processor")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    add_parser = subparsers.add_parser("add", help="Add a value")
    subtract_parser = subparsers.add_parser("subtract", help="Subtract a value")
    multiply_parser = subparsers.add_parser("multiply", help="Multiply by factor")
    divide_parser = subparsers.add_parser("divide", help="Divide result")
    add_parser.add_argument("--value", type=int, required=True)
    subtract_parser.add_argument("--value", type=float, required=True)
    multiply_parser.add_argument("--factor", type=int, required=True)
    divide_parser.add_argument("--divisor", type=float, required=True)
    return parser.parse_args()
if __name__ == '__main__':
    try:
        args = parse_args()
        if not hasattr(args, 'command') or args.command is None:
            print("Error: No command provided.")
            exit(1)
        processor = CommandProcessor()
        value_map = {
            "add": ("value", int),
            "subtract": ("value", float),
            "multiply": ("factor", int),
            "divide": ("divisor", float),
        }
        key, validator_type = value_map.get(args.command.lower(), (None, None))
        if not key:
            print("Error: Unknown command.")
            exit(1)
        try:
            val = getattr(args, key)
            validated_val = validator_type(val)
            result = processor.execute(args.command, validated_val)
            print(result)
        except ValueError as ve:
            print(f"Validation error for {args.command}: {str(ve)}")
    except SystemExit:
        pass