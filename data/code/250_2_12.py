def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data1 = (10, 20, 30, 40, 50)
    print(f"The average of {sample_data1} is: {calculate_average(sample_data1)}")
    
    sample_data2 = (5, 15, 25, 35)
    print(f"The average of {sample_data2} is: {calculate_average(sample_data2)}")
    
    sample_data3 = ()
    print(f"The average of {sample_data3} is: {calculate_average(sample_data3)}")