def min_numeric_string(lst):
    return min(float(x) for x in lst)

if __name__ == '__main__':
    sample_values = ['3.14', '2.718', '1.618']
    print(min_numeric_string(sample_values))