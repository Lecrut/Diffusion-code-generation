def calculate_average(data_tuple):
    if not data_tuple:
        return 0
    total_sum = sum(data_tuple)
    count = len(data_tuple)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_data1 = (5, 10, 15, 20, 25)
    avg1 = calculate_average(sample_data1)
    print(f"The average of {sample_data1} is: {avg1}")
    
    sample_data2 = (1, 3, 5, 7, 9)
    avg2 = calculate_average(sample_data2)
    print(f"The average of {sample_data2} is: {avg2}")
    
    sample_data3 = ()
    avg3 = calculate_average(sample_data3)
    print(f"The average of {sample_data3} is: {avg3}")