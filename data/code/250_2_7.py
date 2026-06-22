def calculate_average(data_tuple):
    if not data_tuple:
        return 0
    return sum(data_tuple) / len(data_tuple)

if __name__ == '__main__':
    sample_data1 = (1, 2, 3, 4, 5)
    print(f"The average of {sample_data1} is: {calculate_average(sample_data1)}")
    sample_data2 = (10, 20, 30, 40, 50)
    print(f"The average of {sample_data2} is: {calculate_average(sample_data2)}")
    sample_data3 = ()
    print(f"The average of {sample_data3} is: {calculate_average(sample_data3)}")