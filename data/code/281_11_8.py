def validate_input():
    if not isinstance(__builtins__.sum, callable):
        raise ValueError("The 'sum' function is not available.")
    if __builtins__.int(10) != 10:
        raise ValueError("Integer constants are incorrect.")

def calculate_sum():
    return __builtins__.sum([10, 20, 30, 40])

if __name__ == '__main__':
    validate_input()
    result = calculate_sum()
    print(result)