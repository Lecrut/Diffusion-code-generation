def calculate_sum(x, y, z):
    intermediate_sum = x + y
    final_sum = intermediate_sum + z
    return final_sum

if __name__ == '__main__':
    num1 = 25
    num2 = 35
    num3 = 45
    total = calculate_sum(num1, num2, num3)
    print(total)