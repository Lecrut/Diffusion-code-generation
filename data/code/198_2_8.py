def min_numeric_string(values):
    return str(min(float(value) for value in values))

if __name__ == '__main__':
    sample_values = ["3.14", "2.71", "1.618"]
    print(min_numeric_string(sample_values))