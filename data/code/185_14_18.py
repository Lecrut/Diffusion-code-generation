class KVPairsParser:
    def __init__(self):
        self._result = {}

    @staticmethod
    def _split_pair(pair_str):
        key, value = pair_str.split('=', 1)
        return key.strip(), value.strip()

    def parse(self, kv_string):
        for pair in kv_string.split():
            key, value = self._split_pair(pair)
            self._result[key] = value
        return self._result

if __name__ == '__main__':
    parser = KVPairsParser()
    sample_input = "key1=value1 key2= value2 key1= value3"
    result = parser.parse(sample_input)
    print(result)