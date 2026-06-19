import math

def compare_temperatures(temp1, temp2, tolerance=1e-9):
    if math.isclose(temp1, temp2, rel_tol=tolerance):
        return "equal"
    elif temp1 < temp2:
        return "less than"
    else:
        return "greater than"

if __name__ == '__main__':
    temp_a = 36.600000001
    temp_b = 36.600000000
    result = compare_temperatures(temp_a, temp_b)
    print(result)