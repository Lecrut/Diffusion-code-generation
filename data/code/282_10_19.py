def calculate_sequence_sum(numbers):
    return sum([num for num in numbers])

if __name__ == '__main__':
    data_points = [3, 6, 9, 12, 15]
    total_sum = calculate_sequence_sum(data_points)
    print(total_sum)