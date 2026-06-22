def calculate_average(data_tuple):
    if not data_tuple:
        return 0
    total = sum(data_tuple)
    count = len(data_tuple)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values1 = (2, 4, 6, 8, 10)
    avg1 = calculate_average(sample_values1)
    print(f"The average of {sample_values1} is: {avg1}")

    sample_values2 = (-5, -3, -1, 1, 3, 5)
    avg2 = calculate_average(sample_values2)
    print(f"The average of {sample_values2} is: {avg2}")

    sample_values3 = ()
    avg3 = calculate_average(sample_values3)
    print(f"The average of {sample_values3} is: {avg3}")