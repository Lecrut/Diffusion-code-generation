def filter_above_freezing(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_data = [10.5, -2.3, 0.0, 15.7, -10.1, 0.0, 3.2, -0.5, 20.0]
    result = filter_above_freezing(sample_data)
    print(result)