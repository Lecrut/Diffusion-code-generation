def fetch_indexed_value(source_dict):
    return source_dict["target"][2]

if __name__ == '__main__':
    configuration = {
        "target": [1, 2, 3, 4, 5],
        "source": "default"
    }
    print(fetch_indexed_value(configuration))