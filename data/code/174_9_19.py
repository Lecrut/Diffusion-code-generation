class DictionaryIntersector:
    @staticmethod
    def intersect_dicts(dict1, dict2):
        return {key: value for key, value in dict1.items() if key in dict2}

if __name__ == '__main__':
    sample_dict1 = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    sample_dict2 = {
        "banana": 2,
        "cherry": 4,
        "date": 5
    }
    
    intersection = DictionaryIntersector.intersect_dicts(sample_dict1, sample_dict2)
    print(intersection)