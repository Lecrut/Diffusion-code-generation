import time
def system_converter(input_value):
    if isinstance(input_value, int):
        return input_value * 2
    elif isinstance(input_value, float):
        return input_value / 1.5
    elif isinstance(input_value, str):
        return input_value.upper()
    else:
        return "Invalid input type"
if __name__ == '__main__':
    system_a_input = 10
    system_b_output = system_converter(system_a_input)
    print(f"Input from System A: {system_a_input}")
    print(f"Output for System B: {system_b_output}")
    system_a_input_float = 20.5
    system_b_output_float = system_converter(system_a_input_float)
    print(f"\nInput from System A: {system_a_input_float}")
    print(f"Output for System B: {system_b_output_float}")
    system_a_input_str = "hello world"
    system_b_output_str = system_converter(system_a_input_str)
    print(f"\nInput from System A: '{system_a_input_str}'")
    print(f"Output for System B: '{system_b_output_str}'")
    system_a_input_other = 3.14159
    system_b_output_other = system_converter(system_a_input_other)
    print(f"\nInput from System A: {system_a_input_other}")
    print(f"Output for System B: {system_b_output_other}")