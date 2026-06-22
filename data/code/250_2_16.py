def calculate_average(data_tuple):
    if not data_tuple:
        return 0
    return sum(data_tuple) / len(data_tuple)

if __name__ == '__main__':
    sample_values1 = (10, 20, 30, 40, 50)
    average1 = calculate_average(sample_values1)
    print(f"The average of {sample_values1} is: {average1}")

    sample_values2 = (5, 15, 25, 35)
    average2 = calculate_average(sample_values2)
    print(f"The average of {sample_values2} is: {average2}")

    sample_values3 = ()
    average3 = calculate_average(sample_values3)
    print(f"The average of {sample_values3} is: {average3}")