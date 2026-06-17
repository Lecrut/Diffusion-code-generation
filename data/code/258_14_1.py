def calculate_averages(pairs):
    first_elements = []
    second_elements = []
    for pair in pairs:
        if len(pair) == 2:
            try:
                first_elements.append(float(pair[0]))
                second_elements.append(float(pair[1]))
            except ValueError:
                print(f"Error: Invalid numeric value found in pair {pair}. Skipping.")
        else:
            print(f"Error: Pair {pair} does not contain exactly two elements. Skipping.")
    if first_elements:
        average_first = sum(first_elements) / len(first_elements)
        print(f"Average of the first elements: {average_first}")
    else:
        print("No valid first elements found to calculate the average.")
    if second_elements:
        average_second = sum(second_elements) / len(second_elements)
        print(f"Average of the second elements: {average_second}")
    else:
        print("No valid second elements found to calculate the average.")
if __name__ == '__main__':
    sample_pairs = [
        (10, 20),
        (5, 15),
        (30, 40),
        (7, 'invalid'),
        (1, 2)
    ]
    calculate_averages(sample_pairs)