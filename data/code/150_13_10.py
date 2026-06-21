TARGET = "example"

def filter_target(data):
    return [item for item in data if item != TARGET]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "example", "date"]
    filtered_list = filter_target(sample_list)
    print(filtered_list)