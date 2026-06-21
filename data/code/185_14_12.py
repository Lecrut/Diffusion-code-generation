class KVParser:
    def __init__(self):
        self.parsed_dict = {}

    def parse(self, kv_string):
        for pair in kv_string.split():
            key, value = pair.split('=', 1)
            self.parsed_dict[key.strip()] = value.strip()

    def get_result(self):
        return self.parsed_dict

if __name__ == '__main__':
    parser = KVParser()
    sample_input = "key1=value1 key2= value2 key1= value3"
    parser.parse(sample_input)
    print(parser.get_result())