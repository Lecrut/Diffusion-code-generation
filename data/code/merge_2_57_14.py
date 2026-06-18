import numpy as np
def access_array_directly(arr: list) -> int | float:
    return arr[0]
def validate_and_access(arr: list, index: int = 5) -> tuple[int | float, bool]:
    try:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        value = arr[index]
        return (value, True)
    except IndexError as e:
        print(f"Error: Index out of bounds. {e}")
        return (None, False)
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    direct_result = access_array_directly(sample_array)
    validated_safe, status = validate_and_access(sample_array, index=2)
    if not status:
        print("Validation failed.")
    else:
        print(f"Direct value at 0: {direct_result}")
        print(f"Validated value at 2: {validated_safe}")
    validated_bad, bad_status = validate_and_access(sample_array, index=15)
    if not bad_status:
        print("Access failed as expected for out of bounds.")