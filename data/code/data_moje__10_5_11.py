def print_first_value(data):
    for value in data.values():
        print(value)
        return

sample_dict = {
    "first": 10,
    "second": 20,
    "third": 30
}

if __name__ == "__main__":
    print_first_value(sample_dict)