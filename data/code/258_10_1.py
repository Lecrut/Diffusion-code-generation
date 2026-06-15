import math
def calculate_average_of_all_numbers(data):
    total_sum = 0
    count = 0
    for pair in data:
        for number in pair:
            total_sum += number
            count += 1
    if count == 0:
        return 0
    return total_sum / count
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4, 5), (6, 7)]
    average = calculate_average_of_all_numbers(sample_data)
    print(average)