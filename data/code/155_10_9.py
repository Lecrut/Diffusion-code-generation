def calculate_list_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result1 = calculate_list_sum(sample_values)
    print(result1)
    
    sample_values = [10.5, 20.5, 30.0]
    result2 = calculate_list_sum(sample_values)
    print(result2)
    
    sample_values = [-1, 5, -3, 10]
    result3 = calculate_list_sum(sample_values)
    print(result3)