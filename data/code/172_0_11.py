class DictionaryMapper:
    def __init__(self, data):
        self.data = data

    def map_values(self):
        return list(self.data.values())

if __name__ == '__main__':
    mapper = DictionaryMapper({
        "apple": "fruit",
        "zebra": "animal",
        "banana": "fruit",
        "cat": "animal",
        "dog": "animal"
    })
    values = mapper.map_values()
    print(values)