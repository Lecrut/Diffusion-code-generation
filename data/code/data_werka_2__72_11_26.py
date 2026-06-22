def check_first_greater(lst):
    indices = {"first": 0, "fifth": 5}
    values = {k: lst[i] for k, i in indices.items()}
    return values["first"] > values["fifth"]

if __name__ == '__main__':
    sample = [10, 20, 30, 40, 50, 5]
    print(check_first_greater(sample))