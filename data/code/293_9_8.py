import time
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
    system_b_result = system_converter(system_a_input)
    print(f"System A Input: {system_a_input}")
    print(f"System B Output: {system_b_result}")
    system_a_input_2 = 10
    system_b_result_2 = system_converter(system_a_input_2)
    print(f"System A Input: {system_a_input_2}")
    print(f"System B Output: {system_b_result_2}")
    system_a_input_3 = 3.14
    system_b_result_3 = system_converter(system_a_input_3)
    print(f"System A Input: {system_a_input_3}")
    print(f"System B Output: {system_b_result_3}")
    system_a_input_4 = [1, 2]
    system_b_result_4 = system_converter(system_a_input_4)
    print(f"System A Input: {system_a_input_4}")
    print(f"System B Output: {system_b_result_4}")