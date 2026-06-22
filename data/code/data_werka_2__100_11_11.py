def verify_boolean_uniformity(data):
    if not data:
        return True
    target = data[0]
    all_match = all(item == target for item in data)
    return all_match

if __name__ == '__main__':
    input_data = [False, False, False, False]
    output = verify_boolean_uniformity(input_data)
    print(output)