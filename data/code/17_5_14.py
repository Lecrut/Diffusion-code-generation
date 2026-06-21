def retrieve_final_item(data):
    length = len(data)
    if length == 0:
        raise IndexError("Cannot retrieve from empty sequence")
    return data[length - 1]

if __name__ == '__main__':
    predefined_values = [100, 200, 300, 400]
    output = retrieve_final_item(predefined_values)
    print(output)