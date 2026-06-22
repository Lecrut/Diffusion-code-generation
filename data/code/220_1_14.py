def calculate_average_of_integers(int_list):
    if not int_list:
        return 0.0
    total_sum = sum(int_list)
    count = len(int_list)
    return total_sum / count

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    average = calculate_average_of_integers(sample_data)
    print(average)