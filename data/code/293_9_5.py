import sys
def system_converter(input_value):
    if isinstance(input_value, str):
        return input_value.upper()
    elif isinstance(input_value, int):
        return input_value * 2
    elif isinstance(input_value, float):
        return input_value + 1.5
    else:
        return "Invalid Input Type"
if __name__ == '__main__':
    system_a_input = "hello world"
    result = system_converter(system_a_input)
    print(f"Input from System A: {system_a_input}")
    print(f"Output for System B: {result}")
    system_a_input_2 = 10
    result_2 = system_converter(system_a_input_2)
    print(f"Input from System A: {system_a_input_2}")
    print(f"Output for System B: {result_2}")
    system_a_input_3 = 3.14
    result_3 = system_converter(system_a_input_3)
    print(f"Input from System A: {system_a_input_3}")
    print(f"Output for System B: {result_3}")