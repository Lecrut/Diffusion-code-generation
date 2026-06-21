def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list1 = [2, 4, 6, 8]
    sample_list2 = [5, 7, 9, 11, 13]
    empty_list = []
    
    avg1 = calculate_average(sample_list1)
    print(f"The average of {sample_list1} is: {avg1}")
    
    avg2 = calculate_average(sample_list2)
    print(f"The average of {sample_list2} is: {avg2}")
    
    avg3 = calculate_average(empty_list)
    if avg3 is None:
        print("The list is empty, no average to compute.")