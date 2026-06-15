import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    numbers = list(map(int, input_data.split()))
    if not numbers:
        mean = 0
    else:
        total_sum = sum(numbers)
        count = len(numbers)
        mean = total_sum / count
    print(f"The numbers read are: {numbers}")
    print(f"The mean is: {mean}")