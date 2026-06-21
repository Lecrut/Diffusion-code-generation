def min_numeric_string(lst):
    return str(min(float(x) for x in lst))

if __name__ == '__main__':
    sample_values = ["3.5", "2.1", "4.8", "1.9"]
    print(min_numeric_string(sample_values))