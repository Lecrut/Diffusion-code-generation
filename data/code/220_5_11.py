ZERO = 0

def calculate_average(list_of_sets):
    total_sum = sum((element for s in list_of_sets for element in s))
    total_count = len([element for s in list_of_sets for element in s])
    if total_count > ZERO:
        return total_sum / total_count
    else:
        return None
if __name__ == '__main__':
    sample_data = [{1, 2, 3}, {4, 5}, {6, 7, 8, 9}]
    average_result = calculate_average(sample_data)
    if average_result is not None:
        print(f'The average of all elements from the sets is: {average_result}')
    else:
        print('No elements found in the provided sets.')