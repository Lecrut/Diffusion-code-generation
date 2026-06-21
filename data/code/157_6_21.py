def find_min(items):
    return min((item for item in items))

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 10]
    print(find_min(sample_values))