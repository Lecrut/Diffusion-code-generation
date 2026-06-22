def calculate_mean(values):
    total_sum = sum(values)
    number_of_elements = len(values)
    mean_value = total_sum / number_of_elements
    return mean_value

if __name__ == '__main__':
    sample_array = [6, 10, 14, 18]
    computed_mean = calculate_mean(sample_array)
    print(computed_mean)