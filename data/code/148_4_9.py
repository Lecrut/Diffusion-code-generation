def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data1 = [3.14, 2.718, 1.618, 0.577]
    sample_data2 = [-5.2, -10.5, -1.0, -20.1]
    sample_data3 = [1.0, 1.0, 1.0, 1.0]
    print(f"Largest in {sample_data1}: {find_largest(sample_data1)}")
    print(f"Largest in {sample_data2}: {find_largest(sample_data2)}")
    print(f"Largest in {sample_data3}: {find_largest(sample_data3)}")