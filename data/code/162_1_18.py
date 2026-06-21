class KeyValueMapper:
    DEFAULT_VALUE = 0

    @staticmethod
    def map_keys_to_values(data):
        result = {}
        for key, value in data.items():
            if isinstance(value, dict):
                result[key] = value
            else:
                result[key] = KeyValueMapper.DEFAULT_VALUE
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
    mapper = KeyValueMapper()
    mapped_values = mapper.map_keys_to_values(sample_data)
    print(mapped_values)