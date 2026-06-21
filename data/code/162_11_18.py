class KeyMapper:
    def __init__(self, keys):
        self.keys = keys

    def map_to_true(self):
        return {key: True for key in self.keys}

if __name__ == '__main__':
    mapper = KeyMapper(['apple', 'banana', 'cherry'])
    result_dict = mapper.map_to_true()
    print(result_dict)