if __name__ == '__main__':
    list_of_sets = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8}
    ]
    total_sum = 0
    total_count = 0
    for s in list_of_sets:
        for element in s:
            total_sum += element
            total_count += 1
    if total_count > 0:
        average = total_sum / total_count
        print(f"The average of all elements from the sets is: {average}")
    else:
        print("No elements found in the provided sets.")