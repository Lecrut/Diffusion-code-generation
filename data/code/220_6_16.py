def calculate_average(set_of_numbers):
    if not set_of_numbers:
        raise ValueError("The input set cannot be empty")
    
    total_sum = sum(set_of_numbers)
    count = len(set_of_numbers)
    
    return total_sum / count

if __name__ == '__main__':
    sample_set = {3, 5, 7}
    average = calculate_average(sample_set)
    print(average)