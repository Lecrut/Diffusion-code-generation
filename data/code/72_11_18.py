def check_first_greater_than_sixth(data):
    indices = {"first": 0, "sixth": 5}
    values = {k: data[v] for k, v in indices.items()}
    return values["first"] > values["sixth"]

if __name__ == '__main__':
    sample_data = [100, 20, 30, 40, 50, 60]
    print(check_first_greater_than_sixth(sample_data))