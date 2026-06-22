def calculate_average_of_sets(list_of_sets):
    total_sum = sum(sum(s) for s in list_of_sets)
    total_count = sum(len(s) for s in list_of_sets)
    if total_count > 0:
        average = total_sum / total_count
        return average
    else:
        raise ValueError("No elements found in the sets.")

if __name__ == '__main__':
    sample_sets = [
        {1, 2, 3},
        {4, 5, 6, 7},
        {8}
    ]
    try:
        avg = calculate_average_of_sets(sample_sets)
        print(f"The average of all elements from the sets is: {avg}")
    except ValueError as e:
        print(e)