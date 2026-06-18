from typing import Literal
def evaluate_condition(value: bool) -> bool:
    return value
if __name__ == '__main__':
    is_raining = True
    has_umbrella = False
    temperature_celsius = 25.0
    condition_a: bool = evaluate_condition(is_raining and not has_umbrella)
    if condition_a or (temperature_celsius > 30):
        result_message: Literal["Go outside", "Stay inside"] = "Stay inside"
    else:
        result_message: Literal["Go outside", "Stay inside"] = "Go outside"
    print(result_message)