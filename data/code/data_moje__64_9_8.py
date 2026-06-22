from enum import Enum

class OperationType(Enum):
    POWER = "power"

def compute_base_power(base_value, exponent_value):
    return base_value ** exponent_value

def execute_operations(op_config, input_data):
    result_map = {
        OperationType.POWER: lambda val: compute_base_power(val["base"], val["exp"])
    }
    return result_map[op_config](input_data)

if __name__ == '__main__':
    sample_inputs = {
        "base": 5,
        "exp": 4
    }
    computed_value = execute_operations(OperationType.POWER, sample_inputs)
    print(computed_value)