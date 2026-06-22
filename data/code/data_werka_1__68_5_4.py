def absolute_differences(sequence):
    previous_value = sequence[0]
    for current_value in sequence[1:]:
        difference = abs(current_value - previous_value)
        yield difference
        previous_value = current_value

if __name__ == '__main__':
    sample_list = [10, 3, 7, 2, 5]
    differences = list(absolute_differences(sample_list))
    print(differences)