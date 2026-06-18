import sys
def calculate_sum(num1, num2, num3):
    return num1 + num2 + num3
if __name__ == '__main__':
    sample_number_1 = 10
    sample_number_2 = 25
    sample_number_3 = 5
    try:
        num1 = int(sample_number_1)
        num2 = int(sample_number_2)
        num3 = int(sample_number_3)
        total_sum = calculate_sum(num1, num2, num3)
        print(total_sum)
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are integers.")