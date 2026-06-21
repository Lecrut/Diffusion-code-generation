def min_numeric_string(values):
    return str(min(float(value) for value in values))

if __name__ == '__main__':
    sample_values = ['3.5', '2.1', '4.8', '1.9']
    print(min_numeric_string(sample_values))