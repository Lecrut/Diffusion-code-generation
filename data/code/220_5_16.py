def calculate_average_of_sets(list_of_sets):
    total_sum = sum(element for s in list_of_sets for element in s)
    total_count = len([element for s in list_of_sets for element in s])
    if total_count > 0:
        average = total_sum / total_count
    else:
        average = 0
    return average

if __name__ == '__main__':
    sample_sets = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    result = calculate_average_of_sets(sample_sets)
    print(f"The average of all elements from the sets is: {result}")