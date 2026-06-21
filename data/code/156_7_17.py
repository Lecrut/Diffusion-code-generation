def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    empty_list = []
    
    avg1 = calculate_average(list1)
    print(f"The average of {list1} is: {avg1}")
    
    avg2 = calculate_average(list2)
    print(f"The average of {list2} is: {avg2}")
    
    avg3 = calculate_average(empty_list)
    if avg3 is None:
        print("Error: Input list cannot be empty")