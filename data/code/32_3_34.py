def total_length_of_strings(strings):
    return sum(len(s) for s in strings)

if __name__ == '__main__':
    sample_values = ["example", "test", "string", "collection"]
    intermediate_result = total_length_of_strings(sample_values)
    print(intermediate_result)