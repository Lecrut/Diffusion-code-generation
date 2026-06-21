def total_length_of_strings(strings):
    length_sum = 0
    for s in strings:
        length_sum += len(s)
    return length_sum

if __name__ == '__main__':
    sample_values = ["data", "science", "machine", "learning"]
    result = total_length_of_strings(sample_values)
    print(result)