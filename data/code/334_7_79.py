class Dictionary:
    def combine(self):
        return " ".join(sorted([k[0], k[1]])) if isinstance(k, tuple) and len(k) == 2 else None
    def __init__(self):
        self.data = {}
    def add_pair(self, word_a, word_b):
        key_tuple = (word_a, word_b)
        combined_value = " ".join(sorted([key_tuple[0], key_tuple[1]]))
        if not isinstance(key_tuple, tuple) or len(key_tuple) != 2:
            return False
        self.data[key_tuple] = combined_value
    def get_combined(self):
        result_dict = {}
        for k in list(self.data.keys()):
            v = " ".join(sorted([k[0], k[1]])) if isinstance(k, tuple) and len(k) == 2 else None
            if v:
                result_dict[k] = v
        return dict(result_dict)
if __name__ == '__main__':
    d = Dictionary()
    d.add_pair("apple", "banana")
    d.add_pair("cat", "dog")
    print(d.get_combined())