def smallest_int_string(strings):
    return min(strings, key=int)

if __name__ == '__main__':
    sample_values = ["3", "15", "2", "9"]
    print(smallest_int_string(sample_values))