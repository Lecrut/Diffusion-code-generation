def compute_average(data_tuple):
    if not data_tuple:
        return 0
    total_sum = sum(data_tuple)
    count = len(data_tuple)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_values1 = (5, 15, 25, 35, 45)
    avg1 = compute_average(sample_values1)
    print(f"The average of {sample_values1} is: {avg1}")
    
    sample_values2 = (-10, -5, 0, 5, 10)
    avg2 = compute_average(sample_values2)
    print(f"The average of {sample_values2} is: {avg2}")
    
    sample_values3 = ()
    avg3 = compute_average(sample_values3)
    print(f"The average of an empty tuple is: {avg3}")