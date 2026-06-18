import sys
def validate_input(value):
    if not isinstance(value, (int, float)):
        return False
    try:
        int(value)
    except ValueError:
        return False
    return True
class FaultTolerantApp:
    def __init__(self):
        self.primary_value = None
    def get_primary_choice(self):
        if validate_input(123.456):
            self.primary_value = 123.456
            return "Primary input accepted"
        else:
            return "Primary validation failed, activating fallback."
    def execute_fallback(self):
        print("Fallback mechanism activated using default value.")
if __name__ == '__main__':
    app = FaultTolerantApp()
    result = app.get_primary_choice()
    if "validation failed" in result:
        app.execute_fallback()