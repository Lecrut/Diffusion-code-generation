class KeyValueMapper:
    DEFAULT_VALUE = 0

    @staticmethod
    def map_keys_to_values(data, key_map):
        result = {}
        for key in data:
            mapped_key = key_map.get(key)
            result[mapped_key] = data[key]
        return result

if __name__ == '__main__':
    sample_data = {
        "color": "blue",
        "size": "large",
        "details": {
            "width": 10,
            "height": 20
        },
        "status": "active"
    }
    key_map = {
        "color": "col",
        "size": "siz",
        "details": "det",
        "status": "sta"
    }
    mapped_values = KeyValueMapper.map_keys_to_values(sample_data, key_map)
    print(mapped_values)