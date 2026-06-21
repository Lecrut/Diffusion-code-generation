class KVParser:
    DELIMITER = '='

    @staticmethod
    def split_key_value(pair):
        return pair.split(KVParser.DELIMITER, 1)

    @staticmethod
    def strip_pair(key, value):
        return key.strip(), value.strip()

    def parse(self, kv_string):
        result = {}
        for pair in kv_string.split():
            key, value = self.split_key_value(pair)
            result[key] = value.strip()
        return result

if __name__ == '__main__':
    parser = KVParser()
    sample_input = "key1=value1 key2= value2 key3=value3"
    print(parser.parse(sample_input))