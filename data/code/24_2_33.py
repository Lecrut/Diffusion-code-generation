def is_negative(x):
    return x < 0

if __name__ == '__main__':
    sample_values = [-10, 0, 5]
    results = {x: is_negative(x) for x in sample_values}
    print(results)