import sys
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    input_data = [10, 20, 30, 40, 50]
    numbers_to_process = []
    for item in input_data:
        try:
            numbers_to_process.append(int(item))
        except ValueError:
            pass
    average = calculate_average(numbers_to_process)
    print(average)