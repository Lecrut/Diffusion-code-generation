class DataItem:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def extract_keys(data_list, keys):
    return [{key: item.__dict__[key] for key in keys if key in item.__dict__} for item in data_list]

if __name__ == '__main__':
    sample_data = [DataItem("Apple", 10), DataItem("Banana", 20), DataItem("Cherry", 30)]
    extracted_data = extract_keys(sample_data, ["name"])
    print(extracted_data)