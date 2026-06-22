def calculate_average(array):
    if not array or len(array) == 0:
        raise ValueError("Array cannot be empty")
    
    total_sum = sum(array)
    total_count = len(array)
    average = total_sum / total_count
    
    return average

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5]
    try:
        avg = calculate_average(sample_array)
        print(f"The average of the array is: {avg}")
    except ValueError as e:
        print(e)