import math

def compare_temperatures(temp1, temp2):
    epsilon = 1e-9
    if math.isclose(temp1, temp2, abs_tol=epsilon):
        return "equal"
    elif temp1 < temp2:
        return "less than"
    else:
        return "greater than"

if __name__ == '__main__':
    temp1 = 23.4567890123456
    temp2 = 23.4567890123457
    result = compare_temperatures(temp1, temp2)
    print(result)