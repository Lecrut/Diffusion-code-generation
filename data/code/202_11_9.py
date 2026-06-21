def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 8]
    print(find_largest(sample_data1))
    
    sample_data2 = [-5, -1, -10, -3]
    print(find_largest(sample_data2))
    
    sample_data3 = [42]
    print(find_largest(sample_data3))
    
    sample_data4 = [7]
    print(find_largest(sample_data4))