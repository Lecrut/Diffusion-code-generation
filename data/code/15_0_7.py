def retrieve_second_last_element(items):
    mapping = {"target": "second_to_last"}
    key = mapping["target"]
    if key == "second_to_last":
        return items[-2]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    result = retrieve_second_last_element(sample_list)
    print(result)