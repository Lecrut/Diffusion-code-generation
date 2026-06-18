import sys
def calculate_sum(num1, num2, num3):
    return num1 + num2 + num3
if __name__ == '__main__':
    sample_number_1 = 10
    sample_number_2 = 25
    sample_number_3 = 5
    try:
        number_a = int(sample_number_1)
        number_b = int(sample_number_2)
        number_c = int(sample_number_3)
        result = calculate_sum(number_a, number_b, number_c)
        print(result)
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are integers.")