# Calculate simple weight difference between two variables
def calculate_weight_difference(var1: float | int, var2: float | int) -> float:
    return abs(var1 - var2)

if __name__ == '__main__':
    a = 50.5
    b = 37.8
    diff = calculate_weight_difference(a, b)
    print(diff)