from typing import Union
def is_positive(value: Union[int, float]) -> bool:
    return value > 0
if __name__ == '__main__':
    sample_values = [42, -7.8, 0, 0.001, float('inf'), -float('inf')]
    for val in sample_values:
        result = is_positive(val)
        print(f"is_positive({val}) = {result}")