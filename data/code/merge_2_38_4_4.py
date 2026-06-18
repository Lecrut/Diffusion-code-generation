def initialize_data():
    data = {}
    data[1] = 42
    data["hello"] = "world"
    return data
if __name__ == '__main__':
    result = initialize_data()
    print(result)