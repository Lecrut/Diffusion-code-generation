def check_first_greater_than_fifth(data):
    if len(data) < 6:
        raise ValueError("List must contain at least 6 elements")
    return data[0] > data[5]

if __name__ == '__main__':
    sample = [100, 2, 3, 4, 5, 50]
    print(check_first_greater_than_fifth(sample))