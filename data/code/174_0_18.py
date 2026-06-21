def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

class DictionaryMerger:
    def __init__(self):
        self.merged_dict = {}

    def add_dict(self, dictionary):
        self.merged_dict.update(dictionary)

    def get_merged_dict(self):
        return self.merged_dict

if __name__ == '__main__':
    merger = DictionaryMerger()
    merger.add_dict({"Alice": 95})
    merger.add_dict({"Bob": 88})
    merger.add_dict({"Charlie": 92, "Bob": 76})
    
    print("--- Merged Dictionary ---")
    print(merger.get_merged_dict())