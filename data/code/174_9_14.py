class DictIntersection:
    @staticmethod
    def intersect(dict1, dict2):
        return {key: dict1[key] for key in dict1 if key in dict2}

if __name__ == '__main__':
    sample_dict1 = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    sample_dict2 = {
        "banana": 4,
        "cherry": 5,
        "date": 6
    }
    intersection_result = DictIntersection.intersect(sample_dict1, sample_dict2)
    print(intersection_result)