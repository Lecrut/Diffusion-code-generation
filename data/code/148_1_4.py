def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [34, 12, 98, 56, 78, 23, 89, 45, 67, 100, 32, 76, 54, 87, 21, 
                     90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 
                     90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78]
    print(find_largest(sample_values))